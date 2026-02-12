#!/usr/bin/env bash
#
# Script: coverage.sh
# Author: Yuqi Huai <yuqi.huai@yourdomain.com>
#
# Description:
#   Generates code coverage reports for the Apollo planning module
#   using DeFT-extracted planning module tests.
#
#   The script runs Bazel coverage with LCOV output, filters
#   instrumentation to //modules/planning, and generates an HTML
#   report using genhtml.
#
# Usage:
#   ./coverage.sh
#
# Output:
#   HTML report generated at:
#     ~/deft/genhtml/index.html
#
# Notes:
#   - Must be run inside an Apollo development container.
#   - Coverage data is produced by //modules/deft:main_test.
#


source /apollo/scripts/apollo_base.sh

bazel coverage -s \
  --combined_report=lcov \
  --instrumentation_filter="^//modules/planning[/:]" \
  //modules/deft:main_test

rm -rf /home/"$USER"/deft/genhtml

genhtml \
  --output /home/"$USER"/deft/genhtml \
  "$(bazel info output_path)/_coverage/_coverage_report.dat"
