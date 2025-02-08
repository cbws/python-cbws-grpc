from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ResourceField(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESOURCE_FIELD_UNSPECIFIED: _ClassVar[ResourceField]
    RESOURCE_FIELD_ORGANIZATION_NAME: _ClassVar[ResourceField]
    RESOURCE_FIELD_PROJECT_NAME: _ClassVar[ResourceField]
    RESOURCE_FIELD_NAME: _ClassVar[ResourceField]
    RESOURCE_FIELD_ORGANIZATION_ID: _ClassVar[ResourceField]
    RESOURCE_FIELD_PROJECT_ID: _ClassVar[ResourceField]
    RESOURCE_FIELD_ID: _ClassVar[ResourceField]
RESOURCE_FIELD_UNSPECIFIED: ResourceField
RESOURCE_FIELD_ORGANIZATION_NAME: ResourceField
RESOURCE_FIELD_PROJECT_NAME: ResourceField
RESOURCE_FIELD_NAME: ResourceField
RESOURCE_FIELD_ORGANIZATION_ID: ResourceField
RESOURCE_FIELD_PROJECT_ID: ResourceField
RESOURCE_FIELD_ID: ResourceField
SERVICE_FIELD_NUMBER: _ClassVar[int]
service: _descriptor.FieldDescriptor
RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
resource_type: _descriptor.FieldDescriptor
ACTION_FIELD_NUMBER: _ClassVar[int]
action: _descriptor.FieldDescriptor
IAM_FIELD_FIELD_NUMBER: _ClassVar[int]
iam_field: _descriptor.FieldDescriptor

class Service(_message.Message):
    __slots__ = ("service",)
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    service: str
    def __init__(self, service: _Optional[str] = ...) -> None: ...
