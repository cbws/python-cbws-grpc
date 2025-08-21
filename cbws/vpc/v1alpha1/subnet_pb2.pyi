from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Subnet(_message.Message):
    __slots__ = ("name", "parent", "prefix", "gateway")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    name: str
    parent: str
    prefix: str
    gateway: str
    def __init__(self, name: _Optional[str] = ..., parent: _Optional[str] = ..., prefix: _Optional[str] = ..., gateway: _Optional[str] = ...) -> None: ...
