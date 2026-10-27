from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LaunchStage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LAUNCH_STAGE_UNSPECIFIED: _ClassVar[LaunchStage]
    LAUNCH_STAGE_PRIVATE_PREVIEW: _ClassVar[LaunchStage]
    LAUNCH_STAGE_PREVIEW: _ClassVar[LaunchStage]
    LAUNCH_STAGE_GA: _ClassVar[LaunchStage]

class ServiceState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SERVICE_STATE_UNSPECIFIED: _ClassVar[ServiceState]
    SERVICE_STATE_DISABLED: _ClassVar[ServiceState]
    SERVICE_STATE_ENABLED: _ClassVar[ServiceState]
LAUNCH_STAGE_UNSPECIFIED: LaunchStage
LAUNCH_STAGE_PRIVATE_PREVIEW: LaunchStage
LAUNCH_STAGE_PREVIEW: LaunchStage
LAUNCH_STAGE_GA: LaunchStage
SERVICE_STATE_UNSPECIFIED: ServiceState
SERVICE_STATE_DISABLED: ServiceState
SERVICE_STATE_ENABLED: ServiceState

class Service(_message.Message):
    __slots__ = ("name", "parent", "config", "state")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    parent: str
    config: ServiceConfig
    state: ServiceState
    def __init__(self, name: _Optional[str] = ..., parent: _Optional[str] = ..., config: _Optional[_Union[ServiceConfig, _Mapping]] = ..., state: _Optional[_Union[ServiceState, str]] = ...) -> None: ...

class ServiceConfig(_message.Message):
    __slots__ = ("name", "title", "launch_stage")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_STAGE_FIELD_NUMBER: _ClassVar[int]
    name: str
    title: str
    launch_stage: LaunchStage
    def __init__(self, name: _Optional[str] = ..., title: _Optional[str] = ..., launch_stage: _Optional[_Union[LaunchStage, str]] = ...) -> None: ...
