from cbws.iam.options.v1alpha1 import options_pb2 as _options_pb2
from cbws.service_management.service_usage.v1alpha1 import service_pb2 as _service_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListServicesRequest(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    def __init__(self, parent: _Optional[str] = ...) -> None: ...

class ListServicesResponse(_message.Message):
    __slots__ = ("services",)
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    services: _containers.RepeatedCompositeFieldContainer[_service_pb2.Service]
    def __init__(self, services: _Optional[_Iterable[_Union[_service_pb2.Service, _Mapping]]] = ...) -> None: ...

class EnableServiceRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class EnableServiceMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EnableServiceResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DisableServiceRequest(_message.Message):
    __slots__ = ("name", "disable_dependent_services")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISABLE_DEPENDENT_SERVICES_FIELD_NUMBER: _ClassVar[int]
    name: str
    disable_dependent_services: bool
    def __init__(self, name: _Optional[str] = ..., disable_dependent_services: bool = ...) -> None: ...

class DisableServiceMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DisableServiceResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
