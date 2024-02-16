from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ToDevice(_message.Message):
    __slots__ = ("request",)
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    request: Request
    def __init__(self, request: _Optional[_Union[Request, _Mapping]] = ...) -> None: ...

class FromDevice(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: Response
    def __init__(self, response: _Optional[_Union[Response, _Mapping]] = ...) -> None: ...

class Request(_message.Message):
    __slots__ = ("get_diagnostics",)
    GET_DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    get_diagnostics: GetDiagnosticsRequest
    def __init__(self, get_diagnostics: _Optional[_Union[GetDiagnosticsRequest, _Mapping]] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ("wifi_get_diagnostics", "dish_get_diagnostics")
    WIFI_GET_DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    DISH_GET_DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    wifi_get_diagnostics: WifiGetDiagnosticsResponse
    dish_get_diagnostics: DishGetDiagnosticsResponse
    def __init__(self, wifi_get_diagnostics: _Optional[_Union[WifiGetDiagnosticsResponse, _Mapping]] = ..., dish_get_diagnostics: _Optional[_Union[DishGetDiagnosticsResponse, _Mapping]] = ...) -> None: ...

class GetDiagnosticsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WifiGetDiagnosticsResponse(_message.Message):
    __slots__ = ("id", "hardware_version", "software_version")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    id: str
    hardware_version: str
    software_version: str
    def __init__(self, id: _Optional[str] = ..., hardware_version: _Optional[str] = ..., software_version: _Optional[str] = ...) -> None: ...

class DishGetDiagnosticsResponse(_message.Message):
    __slots__ = ("id", "hardware_version", "software_version", "utc_offset_s", "hardware_self_test", "alerts", "disablement_code")
    class TestResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_RESULT: _ClassVar[DishGetDiagnosticsResponse.TestResult]
        PASSED: _ClassVar[DishGetDiagnosticsResponse.TestResult]
        FAILED: _ClassVar[DishGetDiagnosticsResponse.TestResult]
    NO_RESULT: DishGetDiagnosticsResponse.TestResult
    PASSED: DishGetDiagnosticsResponse.TestResult
    FAILED: DishGetDiagnosticsResponse.TestResult
    class DisablementCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[DishGetDiagnosticsResponse.DisablementCode]
        OKAY: _ClassVar[DishGetDiagnosticsResponse.DisablementCode]
        NO_ACTIVE_ACCOUNT: _ClassVar[DishGetDiagnosticsResponse.DisablementCode]
        TOO_FAR_FROM_SERVICE_ADDRESS: _ClassVar[DishGetDiagnosticsResponse.DisablementCode]
        IN_OCEAN: _ClassVar[DishGetDiagnosticsResponse.DisablementCode]
        INVALID_COUNTRY: _ClassVar[DishGetDiagnosticsResponse.DisablementCode]
        BLOCKED_COUNTRY: _ClassVar[DishGetDiagnosticsResponse.DisablementCode]
    UNKNOWN: DishGetDiagnosticsResponse.DisablementCode
    OKAY: DishGetDiagnosticsResponse.DisablementCode
    NO_ACTIVE_ACCOUNT: DishGetDiagnosticsResponse.DisablementCode
    TOO_FAR_FROM_SERVICE_ADDRESS: DishGetDiagnosticsResponse.DisablementCode
    IN_OCEAN: DishGetDiagnosticsResponse.DisablementCode
    INVALID_COUNTRY: DishGetDiagnosticsResponse.DisablementCode
    BLOCKED_COUNTRY: DishGetDiagnosticsResponse.DisablementCode
    class Alerts(_message.Message):
        __slots__ = ("dish_is_heating", "dish_thermal_throttle", "dish_thermal_shutdown", "power_supply_thermal_throttle", "motors_stuck", "mast_not_near_vertical", "slow_ethernet_speeds", "software_install_pending", "moving_too_fast_for_policy")
        DISH_IS_HEATING_FIELD_NUMBER: _ClassVar[int]
        DISH_THERMAL_THROTTLE_FIELD_NUMBER: _ClassVar[int]
        DISH_THERMAL_SHUTDOWN_FIELD_NUMBER: _ClassVar[int]
        POWER_SUPPLY_THERMAL_THROTTLE_FIELD_NUMBER: _ClassVar[int]
        MOTORS_STUCK_FIELD_NUMBER: _ClassVar[int]
        MAST_NOT_NEAR_VERTICAL_FIELD_NUMBER: _ClassVar[int]
        SLOW_ETHERNET_SPEEDS_FIELD_NUMBER: _ClassVar[int]
        SOFTWARE_INSTALL_PENDING_FIELD_NUMBER: _ClassVar[int]
        MOVING_TOO_FAST_FOR_POLICY_FIELD_NUMBER: _ClassVar[int]
        dish_is_heating: bool
        dish_thermal_throttle: bool
        dish_thermal_shutdown: bool
        power_supply_thermal_throttle: bool
        motors_stuck: bool
        mast_not_near_vertical: bool
        slow_ethernet_speeds: bool
        software_install_pending: bool
        moving_too_fast_for_policy: bool
        def __init__(self, dish_is_heating: bool = ..., dish_thermal_throttle: bool = ..., dish_thermal_shutdown: bool = ..., power_supply_thermal_throttle: bool = ..., motors_stuck: bool = ..., mast_not_near_vertical: bool = ..., slow_ethernet_speeds: bool = ..., software_install_pending: bool = ..., moving_too_fast_for_policy: bool = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    UTC_OFFSET_S_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_SELF_TEST_FIELD_NUMBER: _ClassVar[int]
    ALERTS_FIELD_NUMBER: _ClassVar[int]
    DISABLEMENT_CODE_FIELD_NUMBER: _ClassVar[int]
    id: str
    hardware_version: str
    software_version: str
    utc_offset_s: int
    hardware_self_test: DishGetDiagnosticsResponse.TestResult
    alerts: DishGetDiagnosticsResponse.Alerts
    disablement_code: DishGetDiagnosticsResponse.DisablementCode
    def __init__(self, id: _Optional[str] = ..., hardware_version: _Optional[str] = ..., software_version: _Optional[str] = ..., utc_offset_s: _Optional[int] = ..., hardware_self_test: _Optional[_Union[DishGetDiagnosticsResponse.TestResult, str]] = ..., alerts: _Optional[_Union[DishGetDiagnosticsResponse.Alerts, _Mapping]] = ..., disablement_code: _Optional[_Union[DishGetDiagnosticsResponse.DisablementCode, str]] = ...) -> None: ...
