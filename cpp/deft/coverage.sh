#!/usr/bin/env bash
#
# Script: coverage.sh
# Author: Yuqi Huai <yuqi.huai@yourdomain.com>
#
# Description:
#   Generates code coverage reports for the Apollo planning module
#   using DeFT-extracted planning module tests.
#
#   Bazel builds and runs the instrumented test, but its own coverage
#   collector invokes gcov without -b and therefore never records branch
#   data. So Bazel's combined report is discarded and the tracefile is
#   captured directly from the .gcno/.gcda pairs the test run leaves
#   behind, with branch coverage enabled.
#
# Usage:
#   ./coverage.sh
#
# Output:
#   LCOV tracefile at:
#     ~/deft/coverage.dat
#   HTML report at:
#     ~/deft/genhtml/index.html
#
# Notes:
#   - Must be run inside an Apollo development container.
#   - Coverage data is produced by //modules/deft:main_test.
#

# Apollo's shell setup reads unset variables, so -u only goes on afterwards.
source /apollo/scripts/apollo_base.sh
set -euo pipefail

OUT_DIR="/home/${USER}/deft"
TRACEFILE="${OUT_DIR}/coverage.dat"
RAW_TRACEFILE="${OUT_DIR}/coverage.raw.dat"
# The counters and the notes that decode them, archived beside the tracefile.
# An LCOV tracefile is a lossy rendering: `BRDA:line,block,branch,taken` keeps
# no record of which outcomes are exception edges rather than decisions, so a
# question like "what is branch coverage over real decisions?" cannot be
# answered from it afterwards -- only by covering every record again, which is
# days of machine time. The raw pair can be re-read with gcov as often as the
# question changes.
GCDA_ARCHIVE="${OUT_DIR}/coverage-gcda.tar.gz"
GCNO_ARCHIVE="${OUT_DIR}/coverage-gcno.tar.gz"

EXECROOT="$(bazel info execution_root)"

# The test writes its .gcda files under COVERAGE_DIR (GCOV_PREFIX), which
# Bazel places at this path inside the execution root, and its collector
# copies the matching .gcno files in beside them. So this directory holds
# everything lcov needs, for the planning module the instrumentation filter
# selected.
COVERAGE_DIR="${EXECROOT}/_coverage/modules/deft/main_test"

# gcov writes its counters when the test exits, so a run that was interrupted
# leaves half-written .gcda behind. Those parse into nonsense -- coverage
# attributed to lines past the end of the file it claims to be -- and the
# capture below would fold them into this run's data. Start from an empty
# directory so only this run's counters are read.
rm -rf "${COVERAGE_DIR}"

bazel coverage -s \
  --instrumentation_filter="^//modules/planning[/:]" \
  //modules/deft:main_test

if [ -z "$(find "${COVERAGE_DIR}" -name '*.gcda' 2>/dev/null | head -1)" ]; then
  echo "No .gcda files found under ${COVERAGE_DIR}; the instrumented test" \
    "did not run." >&2
  exit 1
fi

mkdir -p "${OUT_DIR}"
rm -rf "${OUT_DIR}/genhtml" "${TRACEFILE}" "${RAW_TRACEFILE}"

# gcov records source paths relative to the execution root, so capture from
# there to let lcov and genhtml resolve them.
cd "${EXECROOT}"

lcov --capture \
  --rc lcov_branch_coverage=1 \
  --directory "${COVERAGE_DIR}" \
  --base-directory "${EXECROOT}" \
  --gcov-tool "$(command -v gcov)" \
  --ignore-errors source,graph \
  --output-file "${RAW_TRACEFILE}"

# Drop generated sources (protobuf headers and the like) under bazel-out, so
# the report covers hand-written planning code only.
lcov --remove "${RAW_TRACEFILE}" '*/bazel-out/*' \
  --rc lcov_branch_coverage=1 \
  --ignore-errors source \
  --output-file "${RAW_TRACEFILE}.filtered"

# geninfo records absolute paths that embed the container's Bazel cache hash.
# Rewrite them relative to the workspace, as Bazel's own report had them, so
# tracefiles from different runs and containers stay comparable.
sed -i "s|^SF:${EXECROOT}/|SF:|" "${RAW_TRACEFILE}.filtered"

# Match the instrumentation filter: keep the planning module only.
lcov --extract "${RAW_TRACEFILE}.filtered" '*modules/planning/*' \
  --rc lcov_branch_coverage=1 \
  --ignore-errors source \
  --output-file "${TRACEFILE}"

rm -f "${RAW_TRACEFILE}" "${RAW_TRACEFILE}.filtered"

# Archive the counters and, separately, the notes. They are split because the
# .gcno are identical for every record covered against one build -- archiving
# them per record would multiply the same tens of megabytes by the size of the
# batch -- while the .gcda differ per record and are what has to be kept.
# Paths are stored relative to COVERAGE_DIR so the pair can be unpacked into
# one directory and read by gcov without knowing this container's layout.
rm -f "${GCDA_ARCHIVE}" "${GCNO_ARCHIVE}"
cd "${COVERAGE_DIR}"
for kind in gcda gcno; do
  case "${kind}" in
    gcda) archive="${GCDA_ARCHIVE}" ;;
    gcno) archive="${GCNO_ARCHIVE}" ;;
  esac
  # tar given an empty --files-from writes a valid empty archive and exits 0,
  # so a missing set would survive as a plausible-looking file and only be
  # noticed once the batch it belongs to had already finished. Count first.
  count=$(find . -name "*.${kind}" | wc -l)
  if [ "${count}" -eq 0 ]; then
    echo "No .${kind} files under ${COVERAGE_DIR}; refusing to write an" \
      "empty ${archive}." >&2
    exit 1
  fi
  find . -name "*.${kind}" -print0 | tar --null -czf "${archive}" --files-from=-
  echo "Archived ${count} .${kind} file(s) to ${archive}"
done

# The rewritten paths are workspace-relative, so render from the workspace.
cd /apollo

genhtml \
  --branch-coverage \
  --rc genhtml_branch_coverage=1 \
  --ignore-errors source \
  --output "${OUT_DIR}/genhtml" \
  "${TRACEFILE}"
