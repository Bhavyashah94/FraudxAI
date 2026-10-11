#!/usr/bin/env bash
# Upload the staged FraudxAI India dataset and its description to Kaggle.
#
#     kaggle auth login      # once; credentials live under ~/.kaggle
#     FRAUDX_DATA_DIR=/path/to/staged/files ./upload_kaggle.sh
#
# The data is not tracked in git: FRAUDX_DATA_DIR points at the directory holding
# the *.csv.gz exports. The card, metadata and both manifests are versioned alongside
# this script. The pre-upload `sha256sum -c` fails if the staged data does not match
# the committed manifest.
#
# Process:
#   1. Metadata file must be called dataset-metadata.json.
#   2. Kaggle has no YAML front matter, so the card's --- license block is stripped
#      for Kaggle's description field.
#   3. Uploading data and publishing metadata are two steps:
#      - `datasets version` or `datasets create` uploads the files.
#      - `datasets metadata --update` applies column schemas, cover image, and sources.

set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DATA_DIR="${FRAUDX_DATA_DIR:?set FRAUDX_DATA_DIR to the directory containing the staged *.csv.gz}"
SLUG="${KAGGLE_DATASET_SLUG:-bhavyashah7645/fraudxai-india-100k-seed42}"

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
# Kaggle decompresses .csv.gz on ingest, so the manifest that verifies Kaggle's
# files is the uncompressed one. SHA256SUMS is shipped too so both hosts carry both.
cp "$HERE/SHA256SUMS" "$WORK/"
cp "$HERE/SHA256SUMS_UNCOMPRESSED.txt" "$WORK/"

# Drop resources and image for initial creation/version step
python3 - "$HERE/dataset-metadata.json" "$WORK/dataset-metadata.json" <<'PY'
import json, sys
src, dst = sys.argv[1], sys.argv[2]
m = json.load(open(src))
m.pop("resources", None)
m.pop("image", None)
json.dump(m, open(dst, "w"), indent=2)
PY

cp "$HERE/dataset-metadata.json" "$META_WORK/"
cp "$HERE/dataset-cover-image.png" "$META_WORK/"

# Strip front matter for README
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

# Check if dataset exists
if kaggle datasets status "$SLUG" >/dev/null 2>&1; then
  MODE="version"
  ARGS=(datasets version -p "$WORK" -m "Initial release of FraudxAI India 100k Benchmark" --keep-tabular)
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

# Prove files landed
for _attempt in 1 2 3 4 6; do
  if kaggle datasets files "$SLUG" 2>/dev/null | grep -q "SHA256SUMS_UNCOMPRESSED.txt"; then
    echo "verified: SHA256SUMS_UNCOMPRESSED.txt is in $SLUG"
    echo "done: https://www.kaggle.com/datasets/$SLUG"
    exit 0
  fi
  sleep 10
done

echo "upload reported success but files are still indexing; check:" >&2
echo "  kaggle datasets files $SLUG" >&2
exit 0
