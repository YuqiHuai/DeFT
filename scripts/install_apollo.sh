#!/usr/bin/env bash
set -euo pipefail

# ---- colors ----
GREEN='\033[0;32m'
NC='\033[0m'

# ---- parse argument ----
FULL_BUILD=false
if [[ "${1:-}" == "--full" ]]; then
    FULL_BUILD=true
fi

CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PARENT_DIRECTORY=$(dirname "$CURRENT_DIR")

APOLLO_DIR=$PARENT_DIRECTORY/apollo-7.0.0
GIT_URL="git@github.com:YuqiHuai/BaiduApollo.git"
BRANCH="deft"

# clone Apollo if not cloned
if [ ! -d "$APOLLO_DIR" ]; then
    git clone "$GIT_URL" \
        --branch "$BRANCH" \
        --depth 1 \
        "$APOLLO_DIR"
fi

# Start Apollo
export USER=deft
bash "$APOLLO_DIR/docker/scripts/dev_start.sh"

# Build Apollo (minimal by default)
if [ "$FULL_BUILD" = true ]; then
    echo "Running full build..."
    docker exec -u "$USER" apollo_dev_"$USER" \
        bash /apollo/apollo.sh build
else
    echo "Running minimal build (deft only)..."
    docker exec -u "$USER" apollo_dev_"$USER" \
        bash /apollo/apollo.sh build deft
fi

echo -e "${GREEN}Apollo is now built.${NC}"
