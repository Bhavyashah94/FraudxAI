#!/usr/bin/env bash
# Upload the staged FraudxAI India dataset and its card to Hugging Face.
#
#     FRAUDX_DATA_DIR=/path/to/staged/files HF_TOKEN=hf_... ./upload_hf.sh
#
# The token needs WRITE scope (hf auth login, role Write). It is read from the
# environment only and is never written to disk by this script.
#
# The data is not in the repo: FRAUDX_DATA_DIR points at the directory holding
# the *.csv.gz exports. The card and both checksum manifests are versioned alongside this
# script, and the pre-upload `sha256sum -c` verifies the data before upload.

set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DATA_DIR="${FRAUDX_DATA_DIR:?set FRAUDX_DATA_DIR to the directory containing the staged *.csv.gz}"
REPO="${HF_REPO:-bshah123/fraudxai-india-100k-seed42}"
COMMIT="${HF_COMMIT_MESSAGE:-FraudxAI India 100k seed42: 6 files, 100000 rows each, 2.016% fraud, 44.45-day span}"

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
cp "$HERE/SHA256SUMS" "$WORK/"
cp "$HERE/SHA256SUMS_UNCOMPRESSED.txt" "$WORK/"
cp "$HERE/README.md" "$WORK/README.md"
cp "$HERE/dataset-cover-image.png" "$WORK/"

echo "verifying checksums before upload..."
(cd "$WORK" && sha256sum -c SHA256SUMS)

echo "uploading to $REPO (folder contents land at the repo root)..."
hf upload "$REPO" "$WORK" --repo-type dataset --token "$HF_TOKEN" --commit-message "$COMMIT"

echo "done: https://huggingface.co/datasets/$REPO"
