#!/usr/bin/env bash
set -euo pipefail

if [ -z "${ACCOUNT_ID:-}" ] || [ -z "${REGION:-}" ]; then
  echo "Please set ACCOUNT_ID and REGION environment variables"
  echo "Example: ACCOUNT_ID=123... REGION=us-east-1 ./scripts/push-to-ecr.sh"
  exit 1
fi

IMAGE_NAME="myproductionapp"
TAG=$(git rev-parse --short HEAD)
ECR_URI="${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/${IMAGE_NAME}"

docker build -f Dockerfile.prod -t "${IMAGE_NAME}:local" .
docker tag "${IMAGE_NAME}:local" "${ECR_URI}:${TAG}"

aws ecr create-repository --repository-name "${IMAGE_NAME}" --region "${REGION}" 2>/dev/null || true
aws ecr get-login-password --region "${REGION}" | docker login --username AWS --password-stdin "${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com"
docker push "${ECR_URI}:${TAG}"

echo "Pushed ${ECR_URI}:${TAG}"
