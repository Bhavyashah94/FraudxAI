#!/usr/bin/env bash
# Upload the staged FraudxAI dataset and its description to Kaggle.
#
#     kaggle auth login      # once; the token lives under ~/.kaggle
#     FRAUDX_DATA_DIR=/path/to/staged/files ./upload_kaggle.sh
#
# The ~60 MB of data is not in the repo: FRAUDX_DATA_DIR points at the directory holding
# the *.csv.gz exports. The card, the metadata and both manifests are versioned alongside
# this script; the pre-upload `sha256sum -c` fails if the staged data no longer matches
# the committed manifest, so the two cannot drift apart silently.
#
# Three things this script has to get right:
#
#   1. The metadata file must be called dataset-metadata.json. That is what
#      kaggle.api.kaggle_api_extended.DATASET_METADATA_FILE is set to; the
#      `kaggle datasets create --help` text says "datasets-metadata.json" and is wrong.
#   2. Kaggle has no YAML front matter, so the card's --- license block is stripped here
#      instead of maintaining a second copy of the card that can drift from the first.
#   3. Uploading the data and publishing the description are two different commands, and
#      they disagree about what a resource path means. `datasets version` only *validates*
#      resources -- it never sends them -- and it checks them against the files sitting in
#      the local folder, which are named *.csv.gz. `datasets metadata --update` is the
#      only call that actually applies resources, the cover image, userSpecifiedSources
#      and expectedUpdateFrequency, and it checks paths against Kaggle's *stored* names,
#      which are decompressed *.csv. So the committed metadata uses .csv, the version
#      step strips resources entirely, and the metadata step re-applies them.
#
#      Skipping step 2 is how the column descriptions silently never reached Kaggle.

set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DATA_DIR="${FRAUDX_DATA_DIR:?set FRAUDX_DATA_DIR to the directory containing the staged *.csv.gz}"
SLUG="${KAGGLE_DATASET_SLUG:-bhavyashah7645/fraudxai-us-100k-seed42}"

if ! command -v kaggle >/dev/null 2>&1; then
  echo "kaggle CLI not found on PATH (pip install -U kaggle)" >&2
  exit 1
fi

if ! ls "$DATA_DIR"/*.csv.gz >/dev/null 2>&1; then
  echo "no *.csv.gz found in FRAUDX_DATA_DIR=$DATA_DIR" >&2
  exit 1
fi

grep -q "\"$SLUG\"" "$HERE/dataset-metadata.json" || {
  echo "dataset-metadata.json does not declare id $SLUG; update it or set KAGGLE_DATASET_SLUG" >&2
  exit 1
}

WORK="$(mktemp -d)"
META_WORK="$(mktemp -d)"
trap 'rm -rf "$WORK" "$META_WORK"' EXIT

cp "$DATA_DIR"/*.csv.gz "$WORK/"
# Kaggle decompresses .csv.gz on ingest, so the manifest that actually verifies Kaggle's
# files is the uncompressed one; SHA256SUMS is shipped too so both hosts carry both.
cp "$HERE/SHA256SUMS" "$WORK/"
cp "$HERE/SHA256SUMS_UNCOMPRESSED.txt" "$WORK/"

# `datasets version` validates resources against the local *.csv.gz names and the
# committed paths use Kaggle's decompressed *.csv names, so sending them here fails
# outright. It would not apply them anyway -- drop them and re-send below.
python3 - "$HERE/dataset-metadata.json" "$WORK/dataset-metadata.json" <<'PY'
import json, sys
src, dst = sys.argv[1], sys.argv[2]
m = json.load(open(src))
m.pop("resources", None)
m.pop("image", None)
json.dump(m, open(dst, "w"), indent=2)
PY

# The metadata step needs the cover image next to the metadata file; Kaggle crops it
# square for the thumbnail, which is why the generator emits a 1:1 canvas.
cp "$HERE/dataset-metadata.json" "$META_WORK/"
cp "$HERE/dataset-cover-image.png" "$META_WORK/"

# Drop only the leading front matter (first --- ... --- block); later horizontal rules stay,
# and the blank line that followed the block is dropped so the description starts at the title.
awk 'NR == 1 && $0 == "---" { in_fm = 1; next } in_fm && $0 == "---" { in_fm = 0; next } !in_fm' \
  "$HERE/README.md" | sed '/./,$!d' > "$WORK/README.md"

if head -5 "$WORK/README.md" | grep -q '^license:'; then
  echo "front matter strip failed; README.md still opens with the YAML block" >&2
  exit 1
fi
grep -q -m1 '^# FraudxAI' "$WORK/README.md" || {
  echo "front matter strip failed; README.md does not open with the card title" >&2
  exit 1
}

echo "verifying checksums before upload..."
(cd "$WORK" && sha256sum -c SHA256SUMS)

# --keep-tabular: without it Kaggle re-writes tabular files, which would change the bytes
# and make the manifests useless to whoever downloads them.
#
# Two traps this has to work around:
#   * `kaggle datasets create` exits 0 even when it refuses the upload (a title already in
#     use), so the message has to be inspected -- the exit code proves nothing.
#   * An existing dataset cannot be re-created, so an update goes through `datasets version`.
if kaggle datasets status "$SLUG" >/dev/null 2>&1; then
  MODE="version"
  ARGS=(datasets version -p "$WORK" -m "Checksum manifests for both hosts" --keep-tabular)
else
  MODE="create"
  ARGS=(datasets create -p "$WORK" --public --keep-tabular)
fi

echo "uploading to $SLUG ($MODE) ..."
OUTPUT="$(kaggle "${ARGS[@]}" 2>&1)" || RC="$?"
RC="${RC:-0}"
printf '%s\n' "$OUTPUT"

if [ "$RC" -ne 0 ] || printf '%s' "$OUTPUT" | grep -qiE "creation error|internal error|is already in use"; then
  echo "kaggle refused the upload (mode $MODE)" >&2
  exit 1
fi

# Second half of the publish: the column schemas, cover image, source URL and update
# frequency. `datasets metadata --update` exits non-zero when Kaggle rejects any of it --
# an invalid keyword or a resource path that matches no stored file aborts the whole call
# -- so the exit code here is meaningful and is checked.
#
# The keywords in dataset-metadata.json are Kaggle's controlled vocabulary only. Kaggle
# rejects fraud-detection / synthetic-data / payment-fraud / iso-8583 as tags, and one
# rejected keyword fails the entire settings update, which would also drop the schemas.
# Those domain tags still reach Hugging Face, whose front matter accepts them.
echo "publishing schemas, cover image and sources..."
META_OUT="$(kaggle datasets metadata "$SLUG" --update -p "$META_WORK" 2>&1)" || META_RC="$?"
META_RC="${META_RC:-0}"
printf '%s\n' "$META_OUT"
if [ "$META_RC" -ne 0 ] || printf '%s' "$META_OUT" | grep -qiE "invalid|does not contain a file named"; then
  echo "kaggle refused the metadata update; schemas/image/sources were NOT applied" >&2
  exit 1
fi
printf '%s' "$META_OUT" | grep -q "successfully updated dataset metadata" || {
  echo "metadata update did not report success; check the output above" >&2
  exit 1
}

# Prove the files landed rather than trusting the message: README.md is the file this run
# must have uploaded, and Kaggle takes a moment to index new files.
for _attempt in 1 2 3 4 5 6; do
  if kaggle datasets files "$SLUG" 2>/dev/null | grep -q "SHA256SUMS_UNCOMPRESSED.txt"; then
    echo "verified: SHA256SUMS_UNCOMPRESSED.txt is in $SLUG"
    echo "done: https://www.kaggle.com/datasets/$SLUG"
    exit 0
  fi
  sleep 10
done

echo "upload reported success but SHA256SUMS_UNCOMPRESSED.txt is not listed yet; check:" >&2
echo "  kaggle datasets files $SLUG" >&2
exit 1
