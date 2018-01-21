# gRPC demo

## Setup dev and client/server environments

1. Install Python
2. Install grpcio-tools module: `pip install grpcio-tools` (prefer using virtualenv)

## Generate client/server stub

```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. task_gateway.proto
```

## Run server

```
python task_gateway_server.py
```

## Run client

```
python task_gateway_client.py
```
