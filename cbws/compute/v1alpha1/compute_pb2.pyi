from cbws.compute.v1alpha1 import machine_pb2 as _machine_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListMachinesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "read_mask")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListMachinesResponse(_message.Message):
    __slots__ = ("machines", "next_page_token")
    MACHINES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    machines: _containers.RepeatedCompositeFieldContainer[_machine_pb2.Machine]
    next_page_token: str
    def __init__(self, machines: _Optional[_Iterable[_Union[_machine_pb2.Machine, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetMachineRequest(_message.Message):
    __slots__ = ("name", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class RequestMachineConsoleRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class RequestMachineConsoleResponse(_message.Message):
    __slots__ = ("protocol", "type", "url")
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    protocol: str
    type: str
    url: str
    def __init__(self, protocol: _Optional[str] = ..., type: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...

class CreateMachineRequest(_message.Message):
    __slots__ = ("parent", "machine_id", "machine")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    MACHINE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    machine_id: str
    machine: _machine_pb2.Machine
    def __init__(self, parent: _Optional[str] = ..., machine_id: _Optional[str] = ..., machine: _Optional[_Union[_machine_pb2.Machine, _Mapping]] = ...) -> None: ...

class CreateMachineResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateMachineMetadata(_message.Message):
    __slots__ = ("state", "machine")
    STATE_FIELD_NUMBER: _ClassVar[int]
    MACHINE_FIELD_NUMBER: _ClassVar[int]
    state: _machine_pb2.Machine.State
    machine: _machine_pb2.Machine
    def __init__(self, state: _Optional[_Union[_machine_pb2.Machine.State, str]] = ..., machine: _Optional[_Union[_machine_pb2.Machine, _Mapping]] = ...) -> None: ...

class StopMachineRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class StopMachineResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StopMachineMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StartMachineRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class StartMachineResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StartMachineMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResetMachineRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ResetMachineResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResetMachineMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReinstallMachineRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ReinstallMachineResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReinstallMachineMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteMachineRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteMachineMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
