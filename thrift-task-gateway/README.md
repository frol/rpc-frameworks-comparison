# Thrift demo

## Generate client/server stub

```
docker run --rm -v "$PWD:/data" thrift thrift -o /data --gen py /data/task_gateway.thrift
```

## Setup client/server environments

1. Install Python
2. Install thrift library: `pip install thrift` (prefer using virtualenv)

## Run server

```
python task_gateway_server.py
```

## Run client

```
python task_gateway_client.py
```
