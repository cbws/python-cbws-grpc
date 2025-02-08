from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Policy(_message.Message):
    __slots__ = ("bindings", "etag")
    BINDINGS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    bindings: _containers.RepeatedCompositeFieldContainer[Binding]
    etag: bytes
    def __init__(self, bindings: _Optional[_Iterable[_Union[Binding, _Mapping]]] = ..., etag: _Optional[bytes] = ...) -> None: ...

class Binding(_message.Message):
    __slots__ = ("role", "description", "members")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    role: str
    description: str
    members: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, role: _Optional[str] = ..., description: _Optional[str] = ..., members: _Optional[_Iterable[str]] = ...) -> None: ...
