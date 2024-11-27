from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SystemInfo(_message.Message):
    __slots__ = ("nodeID", "nodeDescription", "statusMsg")
    NODEID_FIELD_NUMBER: _ClassVar[int]
    NODEDESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATUSMSG_FIELD_NUMBER: _ClassVar[int]
    nodeID: int
    nodeDescription: str
    statusMsg: str
    def __init__(self, nodeID: _Optional[int] = ..., nodeDescription: _Optional[str] = ..., statusMsg: _Optional[str] = ...) -> None: ...

class Sensors(_message.Message):
    __slots__ = ("tankLevel", "tankTemp", "dutFlow", "pumpTemp", "pumpSpeed", "dutPressIn", "dutPressOut", "dutTemp", "sumpLevel", "ambientTemp", "ambientPress")
    TANKLEVEL_FIELD_NUMBER: _ClassVar[int]
    TANKTEMP_FIELD_NUMBER: _ClassVar[int]
    DUTFLOW_FIELD_NUMBER: _ClassVar[int]
    PUMPTEMP_FIELD_NUMBER: _ClassVar[int]
    PUMPSPEED_FIELD_NUMBER: _ClassVar[int]
    DUTPRESSIN_FIELD_NUMBER: _ClassVar[int]
    DUTPRESSOUT_FIELD_NUMBER: _ClassVar[int]
    DUTTEMP_FIELD_NUMBER: _ClassVar[int]
    SUMPLEVEL_FIELD_NUMBER: _ClassVar[int]
    AMBIENTTEMP_FIELD_NUMBER: _ClassVar[int]
    AMBIENTPRESS_FIELD_NUMBER: _ClassVar[int]
    tankLevel: float
    tankTemp: float
    dutFlow: float
    pumpTemp: float
    pumpSpeed: float
    dutPressIn: float
    dutPressOut: float
    dutTemp: float
    sumpLevel: float
    ambientTemp: float
    ambientPress: float
    def __init__(self, tankLevel: _Optional[float] = ..., tankTemp: _Optional[float] = ..., dutFlow: _Optional[float] = ..., pumpTemp: _Optional[float] = ..., pumpSpeed: _Optional[float] = ..., dutPressIn: _Optional[float] = ..., dutPressOut: _Optional[float] = ..., dutTemp: _Optional[float] = ..., sumpLevel: _Optional[float] = ..., ambientTemp: _Optional[float] = ..., ambientPress: _Optional[float] = ...) -> None: ...

class Valves(_message.Message):
    __slots__ = ("tankFillIV", "tankOutIV", "tankDrainIV", "dutInIV", "dutOutIV", "sumpDrainIV")
    TANKFILLIV_FIELD_NUMBER: _ClassVar[int]
    TANKOUTIV_FIELD_NUMBER: _ClassVar[int]
    TANKDRAINIV_FIELD_NUMBER: _ClassVar[int]
    DUTINIV_FIELD_NUMBER: _ClassVar[int]
    DUTOUTIV_FIELD_NUMBER: _ClassVar[int]
    SUMPDRAINIV_FIELD_NUMBER: _ClassVar[int]
    tankFillIV: bool
    tankOutIV: bool
    tankDrainIV: bool
    dutInIV: bool
    dutOutIV: bool
    sumpDrainIV: bool
    def __init__(self, tankFillIV: bool = ..., tankOutIV: bool = ..., tankDrainIV: bool = ..., dutInIV: bool = ..., dutOutIV: bool = ..., sumpDrainIV: bool = ...) -> None: ...

class Controls(_message.Message):
    __slots__ = ("pumpEnable", "pumpDemand", "sumppumpEnable")
    PUMPENABLE_FIELD_NUMBER: _ClassVar[int]
    PUMPDEMAND_FIELD_NUMBER: _ClassVar[int]
    SUMPPUMPENABLE_FIELD_NUMBER: _ClassVar[int]
    pumpEnable: bool
    pumpDemand: float
    sumppumpEnable: bool
    def __init__(self, pumpEnable: bool = ..., pumpDemand: _Optional[float] = ..., sumppumpEnable: bool = ...) -> None: ...

class SetSysInfoRequest(_message.Message):
    __slots__ = ("system_info",)
    SYSTEM_INFO_FIELD_NUMBER: _ClassVar[int]
    system_info: SystemInfo
    def __init__(self, system_info: _Optional[_Union[SystemInfo, _Mapping]] = ...) -> None: ...

class SetSysInfResult(_message.Message):
    __slots__ = ("system_info",)
    SYSTEM_INFO_FIELD_NUMBER: _ClassVar[int]
    system_info: SystemInfo
    def __init__(self, system_info: _Optional[_Union[SystemInfo, _Mapping]] = ...) -> None: ...

class GetSysInfRequest(_message.Message):
    __slots__ = ("request",)
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    request: bool
    def __init__(self, request: bool = ...) -> None: ...

class GetSysInfResult(_message.Message):
    __slots__ = ("system_info",)
    SYSTEM_INFO_FIELD_NUMBER: _ClassVar[int]
    system_info: SystemInfo
    def __init__(self, system_info: _Optional[_Union[SystemInfo, _Mapping]] = ...) -> None: ...

class SetValveRequest(_message.Message):
    __slots__ = ("valves",)
    VALVES_FIELD_NUMBER: _ClassVar[int]
    valves: Valves
    def __init__(self, valves: _Optional[_Union[Valves, _Mapping]] = ...) -> None: ...

class SetValveResult(_message.Message):
    __slots__ = ("valves",)
    VALVES_FIELD_NUMBER: _ClassVar[int]
    valves: Valves
    def __init__(self, valves: _Optional[_Union[Valves, _Mapping]] = ...) -> None: ...

class GetValveRequest(_message.Message):
    __slots__ = ("request",)
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    request: bool
    def __init__(self, request: bool = ...) -> None: ...

class GetValveResult(_message.Message):
    __slots__ = ("valves",)
    VALVES_FIELD_NUMBER: _ClassVar[int]
    valves: Valves
    def __init__(self, valves: _Optional[_Union[Valves, _Mapping]] = ...) -> None: ...

class GetSensorRequest(_message.Message):
    __slots__ = ("request",)
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    request: bool
    def __init__(self, request: bool = ...) -> None: ...

class GetSensorResult(_message.Message):
    __slots__ = ("sensors",)
    SENSORS_FIELD_NUMBER: _ClassVar[int]
    sensors: Sensors
    def __init__(self, sensors: _Optional[_Union[Sensors, _Mapping]] = ...) -> None: ...

class SetControlRequest(_message.Message):
    __slots__ = ("controls",)
    CONTROLS_FIELD_NUMBER: _ClassVar[int]
    controls: Controls
    def __init__(self, controls: _Optional[_Union[Controls, _Mapping]] = ...) -> None: ...

class SetControlResult(_message.Message):
    __slots__ = ("controls",)
    CONTROLS_FIELD_NUMBER: _ClassVar[int]
    controls: Controls
    def __init__(self, controls: _Optional[_Union[Controls, _Mapping]] = ...) -> None: ...

class GetControlRequest(_message.Message):
    __slots__ = ("request",)
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    request: bool
    def __init__(self, request: bool = ...) -> None: ...

class GetControlResult(_message.Message):
    __slots__ = ("controls",)
    CONTROLS_FIELD_NUMBER: _ClassVar[int]
    controls: Controls
    def __init__(self, controls: _Optional[_Union[Controls, _Mapping]] = ...) -> None: ...
