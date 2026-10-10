#!/usr/bin/env bash
# Upload the staged FraudxAI dataset and its card to Hugging Face.
#
#     FRAUDX_DATA_DIR=/path/to/staged/files HF_TOKEN=hf_... ./upload_hf.sh
#
# The token needs WRITE scope (hf auth login, role Write). It is read from the
# environment only and is never written to disk by this script.
#
# The ~60 MB of data is not in the repo: FRAUDX_DATA_DIR points at the directory holding
# the *.csv.gz exports. The card and both checksum manifests are versioned alongside this
# script, and the pre-upload `sha256sum -c` is what ties the two together -- uploading data
# that no longer matches the committed manifest fails before anything leaves the machine.

set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DATA_DIR="${FRAUDX_DATA_DIR:?set FRAUDX_DATA_DIR to the directory containing the staged *.csv.gz}"
REPO="${HF_REPO:-bshah123/fraudxai-us-100k-seed42}"
COMMIT="${HF_COMMIT_MESSAGE:-FraudxAI US 100k seed42: 6 files, 100000 rows each, 2.009% fraud}"

: "${HF_TOKEN:?set HF_TOKEN to a Hugging Face write token}"

if ! command -v hf >/dev/null 2>&1; then
  echo "hf CLI not found on PATH (pip install -U huggingface_hub)" >&2
  exit 1
fi
if ! ls "$DATA_DIR"/*.csv.gz >/dev/null 2>&1; then
  echo "no *.csv.gz found in FRAUDX_DATA_DIR=$DATA_DIR" >&2
  exit 1
fi

WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

cp "$DATA_DIR"/*.csv.gz "$WORK/"
# SHA256SUMS covers the .gz bytes uploaded here; the uncompressed manifest lets someone
# who re-exports from the source repo verify the same data without a round trip.
cp "$HERE/SHA256SUMS" "$WORK/"
cp "$HERE/SHA256SUMS_UNCOMPRESSED.txt" "$WORK/"
# The card keeps its YAML front matter: that is how Hugging Face reads license and tags.
cp "$HERE/README.md" "$WORK/README.md"

echo "verifying checksums before upload..."
(cd "$WORK" && sha256sum -c SHA256SUMS)

echo "uploading to $REPO (folder contents land at the repo root)..."
hf upload "$REPO" "$WORK" --repo-type dataset --token "$HF_TOKEN" --commit-message "$COMMIT"

echo "done: https://huggingface.co/datasets/$REPO"
