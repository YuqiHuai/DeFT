#!/usr/bin/env bash
set -euo pipefail

# Provision one Apollo checkout per parallel coverage worker.
#
# `deft coverage` mutates the Apollo tree while it runs: it rewrites
# planning.conf and the per-scenario textprotos to replay a record under the
# configuration it was executed with, and points the HD-map flagfile at that
# record's map. /apollo is a bind mount of the checkout, so workers sharing one
# tree would overwrite each other's configuration mid-run. The tree also holds
# the Bazel output base the instrumented test writes its coverage data to, and
# two Bazel servers against one output base corrupt it. Hence one copy each.
#
# Copies keep .cache/bazel, which holds the instrumented build. It stays valid
# in every copy because Bazel keys the output base on the workspace path, which
# is /apollo inside every container regardless of where the copy lives on the
# host, so no worker has to rebuild.
#
# Usage:
#   scripts/provision_workers.sh [--workers N] [--dest DIR] [--source DIR]
#                                [--force] [--dry-run]

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m'

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

workers=4
source_dir="${PROJECT_DIR}/apollo-7.0.0"
dest_dir="$(dirname "${PROJECT_DIR}")/deft-apollo-workers"
force="no"
dry_run="no"

usage() {
  sed -n '3,26p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'
  exit "${1:-0}"
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --workers) workers="$2"; shift 2 ;;
    --dest)    dest_dir="$2"; shift 2 ;;
    --source)  source_dir="$2"; shift 2 ;;
    --force)   force="yes"; shift ;;
    --dry-run) dry_run="yes"; shift ;;
    -h|--help) usage 0 ;;
    *) echo -e "${RED}unknown option: $1${NC}" >&2; usage 2 ;;
  esac
done

if ! [[ "${workers}" =~ ^[0-9]+$ ]] || (( workers < 1 || workers > 8 )); then
  echo -e "${RED}Error: --workers must be between 1 and 8${NC}" >&2; exit 2
fi
if [[ ! -d "${source_dir}/modules/deft" ]]; then
  echo -e "${RED}Error: ${source_dir} is not a DeFT Apollo checkout${NC}" >&2
  echo "Run scripts/install_apollo.sh first." >&2; exit 1
fi
# Copies carry the build, so an out-of-date source tree means every worker
# rebuilds the instrumented planning module independently on its first record --
# correct, but paid N times over and all at once. Copying mid-build is worse: the
# cache can be captured half-written.
if [[ ! -d "${source_dir}/.cache/bazel" ]]; then
  echo -e "${YELLOW}Warning: ${source_dir}/.cache/bazel is missing.${NC}"
  echo "Every worker would rebuild the instrumented planning module on its first"
  echo "record. Run 'uv run deft coverage <record>' once before provisioning."
  echo
else
  # `| head -1` would exit on the first line and SIGPIPE the writer, which
  # pipefail turns into a 141 the script dies on. awk drains its input instead.
  newest() { awk '$1 > m { m = $1 } END { if (m != "") print m }'; }
  newest_src=$(find "${source_dir}/modules/planning" "${source_dir}/modules/deft" \
    \( -name '*.cc' -o -name '*.h' -o -name 'BUILD' \) -printf '%T@\n' 2>/dev/null \
    | newest)
  newest_build=$(find "${source_dir}/.cache/bazel" -path '*bin/modules/deft*' \
    -printf '%T@\n' 2>/dev/null | newest)
  if [[ -z "${newest_build}" ]]; then
    echo -e "${YELLOW}Warning: no built //modules/deft outputs in the Bazel cache.${NC}"
    echo "Run 'uv run deft coverage <record>' once so the copies carry the build."
    echo
  elif [[ -n "${newest_src}" ]] && \
       (( $(printf '%.0f' "${newest_src}") > $(printf '%.0f' "${newest_build}") )); then
    echo -e "${YELLOW}Warning: sources are newer than the built outputs.${NC}"
    echo "  newest source: $(date -d "@${newest_src%%.*}" '+%F %T')"
    echo "  newest build : $(date -d "@${newest_build%%.*}" '+%F %T')"
    echo "Each worker would rebuild separately. Run 'uv run deft coverage <record>'"
    echo "once to refresh the build, then provision."
    echo
  fi
fi
if pgrep -f "bazel.*${source_dir##*/}" >/dev/null 2>&1; then
  echo -e "${YELLOW}Warning: a Bazel process is running against the source tree.${NC}"
  echo "Copying now may capture a half-written cache. Let it finish first."
  echo
fi
source_dir="$(cd "${source_dir}" && pwd)"

# Dropped: history and caches only needed to build, plus runtime debris. The
# core dumps in particular are large and are left behind by crashed replays.
excludes=(
  --exclude "/.git"
  --exclude "/.cache/build/"
  --exclude "/.cache/repos/"
  --exclude "/data/log/"
  --exclude "/data/bag/"
  --exclude "/data/core/"
  --exclude "/docs/"
  --exclude "/nohup.out"
  --exclude "/.dev_bash_hist"
)

# rsync -a implies -o/-g, which fails on root-owned files a previous run left
# behind. Ownership does not matter: containers write into a user-owned mount.
rsync_flags=(-rlptD --no-owner --no-group --delete-during)
[[ -t 1 ]] && rsync_flags+=(--info=progress2)

echo "source:  ${source_dir}"
echo "dest:    ${dest_dir}"
echo "workers: ${workers}"
echo

per_copy=$(rsync "${rsync_flags[@]}" "${excludes[@]}" --dry-run --stats \
  "${source_dir}/" "${dest_dir}/.probe/" 2>/dev/null \
  | awk '/Total file size:/ {gsub(/,/,"",$4); print $4; exit}')
rmdir "${dest_dir}/.probe" 2>/dev/null || true
avail=$(df --output=avail -B1 "$(dirname "${dest_dir}")" | tail -1 | tr -d ' ')
need=$(( ${per_copy:-0} * workers ))
human() { numfmt --to=iec --suffix=B "$1" 2>/dev/null || echo "$1"; }
echo "  per copy : $(human "${per_copy:-0}")"
echo "  needed   : $(human "${need}") for ${workers} copies"
echo "  available: $(human "${avail}")"
if (( need > avail )); then
  echo -e "${RED}Error: not enough free space at ${dest_dir}${NC}" >&2; exit 1
fi
echo

mkdir -p "${dest_dir}"
for i in $(seq 1 "${workers}"); do
  # Zero-padded: Apollo's docker/scripts/docker_base.sh matches container names
  # by substring, so an unpadded w1 would also match w10.
  nn="$(printf '%02d' "$i")"
  dest="${dest_dir}/apollo-7.0.0-w${nn}"
  if [[ -d "${dest}" && "${force}" != "yes" ]]; then
    echo -e "${YELLOW}w${nn}: exists, syncing (use --force to recopy)${NC}"
  fi
  if [[ "${dry_run}" == "yes" ]]; then
    echo "would copy -> ${dest}"; continue
  fi
  [[ "${force}" == "yes" ]] && chmod -R u+w "${dest}" 2>/dev/null && rm -rf "${dest}"
  echo "w${nn}: copying -> ${dest}"
  rsync "${rsync_flags[@]}" "${excludes[@]}" "${source_dir}/" "${dest}/"
  echo -e "  ${GREEN}done${NC}: $(du -sh "${dest}" | cut -f1)"
done

[[ "${dry_run}" == "yes" ]] && exit 0
echo
echo -e "${GREEN}Provisioned ${workers} worker checkout(s) under ${dest_dir}${NC}"
echo "Worker N uses apollo-7.0.0-w<NN> with container user deft_w<NN>."
