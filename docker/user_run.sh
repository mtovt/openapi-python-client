#!/usr/bin/env bash
set -euo pipefail

DOCKER_DIR=$(dirname "$(readlink -f "$0")")

docker build ./.. -f "$DOCKER_DIR/user.dockerfile" -t openapi-python-client && \
docker run -it --rm \
  -w "/opt/generated" \
  -v "$(pwd)/:/opt/generated/" \
  openapi-python-client \
  "$@"


