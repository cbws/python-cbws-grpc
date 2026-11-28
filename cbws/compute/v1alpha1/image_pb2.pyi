from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Image(_message.Message):
    __slots__ = ("name", "parent", "family", "state", "create_time", "source_machine", "source_machine_uid")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Image.State]
        STATE_CREATING: _ClassVar[Image.State]
        STATE_READY: _ClassVar[Image.State]
        STATE_FAILED: _ClassVar[Image.State]
        STATE_DELETING: _ClassVar[Image.State]
    STATE_UNSPECIFIED: Image.State
    STATE_CREATING: Image.State
    STATE_READY: Image.State
    STATE_FAILED: Image.State
    STATE_DELETING: Image.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_MACHINE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_MACHINE_UID_FIELD_NUMBER: _ClassVar[int]
    name: str
    parent: str
    family: str
    state: Image.State
    create_time: _timestamp_pb2.Timestamp
    source_machine: str
    source_machine_uid: str
    def __init__(self, name: _Optional[str] = ..., parent: _Optional[str] = ..., family: _Optional[str] = ..., state: _Optional[_Union[Image.State, str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., source_machine: _Optional[str] = ..., source_machine_uid: _Optional[str] = ...) -> None: ...

class ImageFamily(_message.Message):
    __slots__ = ("name", "parent")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    parent: str
    def __init__(self, name: _Optional[str] = ..., parent: _Optional[str] = ...) -> None: ...
