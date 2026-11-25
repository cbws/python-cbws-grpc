from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MachineAgent(_message.Message):
    __slots__ = ("name", "state", "connect_time", "check_time", "features")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[MachineAgent.State]
        STATE_NOT_INSTALLED: _ClassVar[MachineAgent.State]
        STATE_CONNECTED: _ClassVar[MachineAgent.State]
        STATE_DISCONNECTED: _ClassVar[MachineAgent.State]
        STATE_UNHEALTHY: _ClassVar[MachineAgent.State]
    STATE_UNSPECIFIED: MachineAgent.State
    STATE_NOT_INSTALLED: MachineAgent.State
    STATE_CONNECTED: MachineAgent.State
    STATE_DISCONNECTED: MachineAgent.State
    STATE_UNHEALTHY: MachineAgent.State
    class Feature(_message.Message):
        __slots__ = ("name", "state")
        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_UNSPECIFIED: _ClassVar[MachineAgent.Feature.State]
            STATE_ENABLED: _ClassVar[MachineAgent.Feature.State]
            STATE_DISABLED: _ClassVar[MachineAgent.Feature.State]
            STATE_UNSUPPORTED: _ClassVar[MachineAgent.Feature.State]
        STATE_UNSPECIFIED: MachineAgent.Feature.State
        STATE_ENABLED: MachineAgent.Feature.State
        STATE_DISABLED: MachineAgent.Feature.State
        STATE_UNSUPPORTED: MachineAgent.Feature.State
        NAME_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        name: str
        state: MachineAgent.Feature.State
        def __init__(self, name: _Optional[str] = ..., state: _Optional[_Union[MachineAgent.Feature.State, str]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CONNECT_TIME_FIELD_NUMBER: _ClassVar[int]
    CHECK_TIME_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: MachineAgent.State
    connect_time: _timestamp_pb2.Timestamp
    check_time: _timestamp_pb2.Timestamp
    features: _containers.RepeatedCompositeFieldContainer[MachineAgent.Feature]
    def __init__(self, name: _Optional[str] = ..., state: _Optional[_Union[MachineAgent.State, str]] = ..., connect_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., check_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., features: _Optional[_Iterable[_Union[MachineAgent.Feature, _Mapping]]] = ...) -> None: ...
