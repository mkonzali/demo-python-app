APP?=demo-python-app
IMAGE?=ghcr.io/your-org/$(APP)
TAG?=dev

run:
\tpython app/main.py

test:
\tpytest -q

build:
\tdocker build -t $(IMAGE):$(TAG) .

push:
\tdocker push $(IMAGE):$(TAG)

docker-run:
\tdocker run --rm -p 8080:8080 \
\t  -e APP_VERSION=$(TAG) \
\t  -e GIT_SHA=$$(git rev-parse --short HEAD) \
\t  -e BUILD_DATE=$$(date -u +%Y-%m-%dT%H:%M:%SZ) \
\t  -e IMAGE=$(IMAGE):$(TAG) \
\t  $(IMAGE):$(TAG)
