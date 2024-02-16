# Local Device API
This folder contains information for Starlink's officially supported local API. The local API is a [gRPC](https://grpc.io/) API which is defined in [protobuf](https://protobuf.dev/).

The Starlink router hosts the server at port `9000`. The default subnet for the Starlink router is `192.168.1.1/24`, so the default gRPC server address is `192.168.1.1:9000`.

The Starlink user terminal hosts the server at port `9200`. The Starlink dish is always at `192.168.100.1`.

## Minimum Software Versions
This API requires:
* WiFi router software > 2023.55 (late December 2023)
* User Terminal software > 2023.51.0 (early January 2024)
If your device is not on this software, you may see `UNIMPLEMENTED` API responses.

## API Definition
See `device.proto` for the current API definition. Protobuf is used to resolve backward and forwards compatibility issues. Protobuf can be compiled into different languages. So far we have created a python example implementation.

### Python
#### Compiling
```
$ make python
...
python3 -m grpc_tools.protoc -I . --python_out=. --pyi_out=. --grpc_python_out=. device.proto
```
#### Running
```
$ python demo.py
Sending request to router...
wifi_get_diagnostics {
  id: "Router-010000000000000000012345"
  hardware_version: "v2"
  software_version: "2024.10.0.mr32019"
}

Sending request to dish...
dish_get_diagnostics {
  id: "ut01000000-00000000-00012345"
  hardware_version: "rev3_proto2"
  software_version: "1da5511b-0179-4a9c-80ad-2e63015b5a70.uterm"
  utc_offset_s: -28799
  alerts {
  }
  disablement_code: OKAY
}
```