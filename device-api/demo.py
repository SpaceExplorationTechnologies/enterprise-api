import device_pb2, device_pb2_grpc
import grpc

"""
The Starlink WiFi gRPC server is hosted at port 9000. The Starlink router 
uses the 192.168.1.1/24 by default.
"""
STARLINK_ROUTER_GRPC_ADDR = "192.168.1.1:9000"

"""
The Starlink dish gRPC server is hosted at port 9200. The Starlink dish
is always at 192.168.100.1.
"""
STARLINK_DISH_GRPC_ADDR = "192.168.100.1:9200"

"""
Send the GetDiagnostics request to the given address.
"""
def get_diagnostics(addr: str) -> device_pb2.Response:
    with grpc.insecure_channel(addr) as channel:
        return device_pb2_grpc.DeviceStub(channel).Handle(device_pb2.Request(get_diagnostics=device_pb2.GetDiagnosticsRequest()))

print("Sending request to router...")
try:
    response = get_diagnostics(STARLINK_ROUTER_GRPC_ADDR)
except grpc.RpcError as e:
    print(e.code())
else:
    print(response)

print("Sending request to dish...")
try:
    response = get_diagnostics(STARLINK_DISH_GRPC_ADDR)
except grpc.RpcError as e:
    print(e.code())
else:
    print(response)