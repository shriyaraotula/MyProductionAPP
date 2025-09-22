#!/usr/bin/env bash
set -euo pipefail

# Builds the production image locally (Dockerfile.prod), ensures the app network exists,
# and runs the container attached to that network with DB_HOST=db so it connects to the
# local Postgres container used in this project.

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

IMAGE_NAME="myproductionapp:local"
NETWORK_NAME="leetcode_app_net"
CONTAINER_NAME="myprod"

echo "Building image $IMAGE_NAME from Dockerfile.prod..."
docker build -f Dockerfile.prod -t "$IMAGE_NAME" .

echo "Ensuring Docker network $NETWORK_NAME exists..."
if ! docker network ls --format '{{.Name}}' | grep -q "^${NETWORK_NAME}$"; then
  docker network create "$NETWORK_NAME"
fi

echo "Removing any existing container named $CONTAINER_NAME..."
docker rm -f "$CONTAINER_NAME" 2>/dev/null || true

echo "Starting container $CONTAINER_NAME on network $NETWORK_NAME (DB_HOST=db)..."
docker run -d --name "$CONTAINER_NAME" \
  --network "$NETWORK_NAME" \
  -p 8000:8000 \
  -e ENVIRONMENT=production \
  -e DB_HOST=db \
  "$IMAGE_NAME"

echo "Waiting for /health to be healthy..."
for i in {1..30}; do
  if curl -sS http://localhost:8000/health | grep -q "database"; then
    curl -sS http://localhost:8000/health && break
  fi
  sleep 1
done

echo "Container started. To view logs: docker logs -f $CONTAINER_NAME"
