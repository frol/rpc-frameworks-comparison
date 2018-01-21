# Ice demo

## Setup dev and client/server environments

1. Install Python
2. Install zeroc-ice module: `pip install zeroc-ice` (prefer using virtualenv)

## Generate client/server stub

```
slice2py --underscore task_gateway.ice
```

## Run server

```
python task_gateway_server.py
```

## Run client

```
python task_gateway_client.py
```
