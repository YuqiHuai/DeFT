#!/usr/bin/env bash
set -euo pipefail

# ---- colors ----
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # no color

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

APOLLO_PATH="$SCRIPT_DIR/../apollo-7.0.0"
MAP_SRC="$SCRIPT_DIR/../data/maps"
MAP_DST="$APOLLO_PATH/modules/map/data"

# Check Apollo install
if [[ ! -d "$APOLLO_PATH" ]]; then
  echo -e "${RED}Error: Baidu Apollo 7.0 not installed${NC}"
  exit 1
fi

# Check map data
if [[ ! -d "$MAP_SRC" ]]; then
  echo -e "${RED}Error: Apollo map data not found at ../data/apollo_map${NC}"
  exit 1
fi

# Remove existing map data directory
if [[ -e "$MAP_DST" ]]; then
  echo "Removing existing map data at $MAP_DST"
  rm -rf "$MAP_DST"
fi

# Recreate destination parent directory
mkdir -p "$(dirname "$MAP_DST")"

# Copy map data
cp -a "$MAP_SRC" "$MAP_DST"

echo -e "${GREEN}Map data successfully copied.${NC}"
echo
echo "Installed Apollo maps:"
echo "----------------------"

find "$MAP_DST" -mindepth 1 -maxdepth 1 -type d -printf " - %f\n"
