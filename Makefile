# Makefile: common local and CI helper targets

.PHONY: build-local run-local stop-local push-ecr deploy-k8s

IMAGE_NAME=myproductionapp
TAG=$(shell git rev-parse --short HEAD)

build-local:
	docker build -f Dockerfile.prod -t $(IMAGE_NAME):local .

run-local: build-local
	chmod +x scripts/run-local.sh
	./scripts/run-local.sh

stop-local:
	docker rm -f myprod || true

push-ecr:
	@echo "Provide ACCOUNT_ID and REGION environment variables before running"
	@echo "Example: ACCOUNT_ID=123... REGION=us-east-1 make push-ecr"
	docker tag $(IMAGE_NAME):local $(ACCOUNT_ID).dkr.ecr.$(REGION).amazonaws.com/$(IMAGE_NAME):$(TAG)
	aws ecr get-login-password --region $(REGION) | docker login --username AWS --password-stdin $(ACCOUNT_ID).dkr.ecr.$(REGION).amazonaws.com
	docker push $(ACCOUNT_ID).dkr.ecr.$(REGION).amazonaws.com/$(IMAGE_NAME):$(TAG)

deploy-k8s:
	@echo "Update k8s/production/deployment.yaml image and run kubectl apply -f k8s/production"
