from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MachineType(_message.Message):
    __slots__ = ("name", "zone", "cpu", "memory_mb", "ephemeral_disk_gb")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    CPU_FIELD_NUMBER: _ClassVar[int]
    MEMORY_MB_FIELD_NUMBER: _ClassVar[int]
    EPHEMERAL_DISK_GB_FIELD_NUMBER: _ClassVar[int]
    name: str
    zone: str
    cpu: int
    memory_mb: int
    ephemeral_disk_gb: int
    def __init__(self, name: _Optional[str] = ..., zone: _Optional[str] = ..., cpu: _Optional[int] = ..., memory_mb: _Optional[int] = ..., ephemeral_disk_gb: _Optional[int] = ...) -> None: ...
