from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Project(_message.Message):
    __slots__ = ("name", "display_name", "organization", "unique_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    organization: str
    unique_id: str
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., organization: _Optional[str] = ..., unique_id: _Optional[str] = ...) -> None: ...
