#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
REPO_NAME="$(basename "$REPO_ROOT")"
REPO_PARENT="$(dirname "$REPO_ROOT")"
ARCHIVE_PATH="$REPO_ROOT/${REPO_NAME}-archive.zip"

for required_command in zip unzip; do
  if ! command -v "$required_command" >/dev/null 2>&1; then
    echo "Error: required command '$required_command' was not found." >&2
    exit 1
  fi
done

ARCHIVE_TMP_DIR="$(mktemp -d "${TMPDIR:-/tmp}/deft-archive.XXXXXX")"
ARCHIVE_TMP_PATH="$ARCHIVE_TMP_DIR/${REPO_NAME}-archive.zip"

cleanup() {
  rm -rf "$ARCHIVE_TMP_DIR"
}
trap cleanup EXIT

echo "Creating $ARCHIVE_PATH"

(
  cd "$REPO_PARENT"
  zip -q -r -y "$ARCHIVE_TMP_PATH" "$REPO_NAME" \
    -x "$REPO_NAME/.agents" \
       "$REPO_NAME/.agents/*" \
       "$REPO_NAME/.claude" \
       "$REPO_NAME/.claude/*" \
       "$REPO_NAME/.git" \
       "$REPO_NAME/.git/*" \
       "$REPO_NAME/${REPO_NAME}-archive.zip"
)

if unzip -Z1 "$ARCHIVE_TMP_PATH" \
  | grep -Eq "^${REPO_NAME}/(\.agents|\.claude|\.git)(/|$)"; then
  echo "Error: an excluded directory was found in the archive." >&2
  exit 1
fi

unzip -tq "$ARCHIVE_TMP_PATH"
mv -f "$ARCHIVE_TMP_PATH" "$ARCHIVE_PATH"

echo "Archive entries: $(unzip -Z1 "$ARCHIVE_PATH" | wc -l | tr -d ' ')"
echo "Archive size: $(du -h "$ARCHIVE_PATH" | awk '{print $1}')"

if command -v shasum >/dev/null 2>&1; then
  shasum -a 256 "$ARCHIVE_PATH"
elif command -v sha256sum >/dev/null 2>&1; then
  sha256sum "$ARCHIVE_PATH"
else
  echo "Warning: no SHA-256 utility was found; checksum omitted." >&2
fi
