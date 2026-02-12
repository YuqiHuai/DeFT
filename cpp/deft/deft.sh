#!/usr/bin/env bash
#
# Script: deft.sh
# Author: Yuqi Huai <yhuai@uci.edu>
#
# Description:
#   Runs DeFT-extracted planning module tests by initializing the
#   Apollo environment and invoking the DeFT planning test binary.
#
# Usage:
#   ./deft.sh
#
# Notes:
#   - Must be run inside an Apollo development container.
#   - Relies on DeFT-generated test data under ~/deft/testdata/.
#

source /apollo/scripts/apollo_base.sh

/apollo/bazel-bin/modules/deft/main
