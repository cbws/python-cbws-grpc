# Generated Python gRPC libraries for CBWS

This repository contains the Python package `cbws-grpc`: the messages and the gRPC clients of the public CBWS APIs. A process generates it from the definitions in [cbws/protobufs](https://github.com/cbws/protobufs). Do not change the generated files by hand.

## Installation

To install the package with pip, run this command:

```
pip install cbws-grpc
```

Each API version is a module, for example:

```python
from cbws.compute.v1alpha1 import compute_pb2, compute_pb2_grpc
```

The services accept gRPC with TLS on port 443, for example on `compute.cbws.cloud:443`. Send an access token as the bearer token of each call:

```python
import grpc

credentials = grpc.composite_channel_credentials(
    grpc.ssl_channel_credentials(),
    grpc.access_token_call_credentials(token),
)
with grpc.secure_channel("compute.cbws.cloud:443", credentials) as channel:
    compute = compute_pb2_grpc.ComputeServiceStub(channel)
    response = compute.ListMachineTypes(compute_pb2.ListMachineTypesRequest(parent="zones/-"))
```

## Versions

The tags of this repository have the same version numbers as the tags of [cbws/protobufs](https://github.com/cbws/protobufs). Each commit names the commit of cbws/protobufs it was generated from.

## License

The package is available under the Apache License, Version 2.0. Refer to the `LICENSE` file.
