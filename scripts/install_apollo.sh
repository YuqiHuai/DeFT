#!/usr/bin/env bash
set -euo pipefail

# ---- colors ----
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# ---- defaults ----
FULL_BUILD=false
FORCE_SSH=false
FORCE_HTTPS=false
CLEAN_CLONE=false

SSH_URL="git@github.com:YuqiHuai/BaiduApollo.git"
HTTPS_URL="https://github.com/YuqiHuai/BaiduApollo.git"
BRANCH="deft"

# ---- help ----
usage() {
    echo "Usage: $0 [options]"
    echo ""
    echo "Options:"
    echo "  --full        Run full build"
    echo "  --ssh         Force SSH cloning"
    echo "  --https       Force HTTPS cloning"
    echo "  --clean       Delete existing repo before cloning"
    echo "  -h, --help    Show this help message"
    echo ""
    exit 0
}

# ---- parse args ----
while [[ $# -gt 0 ]]; do
    case "$1" in
        --full)
            FULL_BUILD=true
            ;;
        --ssh)
            FORCE_SSH=true
            ;;
        --https)
            FORCE_HTTPS=true
            ;;
        --clean)
            CLEAN_CLONE=true
            ;;
        -h|--help)
            usage
            ;;
        *)
            echo -e "${RED}Unknown option: $1${NC}"
            usage
            ;;
    esac
    shift
done

# ---- validation ----
if [ "$FORCE_SSH" = true ] && [ "$FORCE_HTTPS" = true ]; then
    echo -e "${RED}Cannot use --ssh and --https together.${NC}"
    exit 1
fi

# ---- directories ----
CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PARENT_DIRECTORY=$(dirname "$CURRENT_DIR")
APOLLO_DIR=$PARENT_DIRECTORY/apollo-7.0.0

# ---- determine git mode ----
echo -e "${YELLOW}Selecting Git access mode...${NC}"

if [ "$FORCE_SSH" = true ]; then
    echo -e "${GREEN}Forcing SSH mode.${NC}"
    GIT_URL="$SSH_URL"

elif [ "$FORCE_HTTPS" = true ]; then
    echo -e "${GREEN}Forcing HTTPS mode.${NC}"
    GIT_URL="$HTTPS_URL"

elif git ls-remote "$SSH_URL" &>/dev/null; then
    echo -e "${GREEN}SSH access confirmed. Using SSH.${NC}"
    GIT_URL="$SSH_URL"

else
    echo -e "${YELLOW}SSH unavailable. Falling back to HTTPS.${NC}"
    GIT_URL="$HTTPS_URL"
fi

# ---- clean if requested ----
if [ "$CLEAN_CLONE" = true ] && [ -d "$APOLLO_DIR" ]; then
    echo -e "${YELLOW}Removing existing repository...${NC}"
    rm -rf "$APOLLO_DIR"
fi

# ---- clone if needed ----
if [ ! -d "$APOLLO_DIR" ]; then
    echo -e "${YELLOW}Cloning Apollo repository...${NC}"
    git clone "$GIT_URL" \
        --branch "$BRANCH" \
        --depth 1 \
        "$APOLLO_DIR"
else
    echo -e "${GREEN}Repository already exists. Skipping clone.${NC}"
fi

# ---- start docker ----
export USER=deft
echo -e "${YELLOW}Starting Apollo Docker environment...${NC}"
bash "$APOLLO_DIR/docker/scripts/dev_start.sh"

# ---- build ----
if [ "$FULL_BUILD" = true ]; then
    echo -e "${YELLOW}Running full build...${NC}"
    docker exec -u "$USER" apollo_dev_"$USER" \
        bash /apollo/apollo.sh build
else
    echo -e "${YELLOW}Running minimal build (deft only)...${NC}"
    docker exec -u "$USER" apollo_dev_"$USER" \
        bash /apollo/apollo.sh build deft
fi

echo -e "${GREEN}Apollo is now built successfully.${NC}"
