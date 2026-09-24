from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Port(_message.Message):
    __slots__ = ("name", "parent", "owner", "ip_families", "ipv4_address", "ipv6_address", "mac_address", "state")
    class IpFamily(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IP_FAMILY_UNSPECIFIED: _ClassVar[Port.IpFamily]
        IP_FAMILY_IPV4: _ClassVar[Port.IpFamily]
        IP_FAMILY_IPV6: _ClassVar[Port.IpFamily]
    IP_FAMILY_UNSPECIFIED: Port.IpFamily
    IP_FAMILY_IPV4: Port.IpFamily
    IP_FAMILY_IPV6: Port.IpFamily
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Port.State]
        STATE_ACTIVE: _ClassVar[Port.State]
    STATE_UNSPECIFIED: Port.State
    STATE_ACTIVE: Port.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    IP_FAMILIES_FIELD_NUMBER: _ClassVar[int]
    IPV4_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    IPV6_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    parent: str
    owner: str
    ip_families: _containers.RepeatedScalarFieldContainer[Port.IpFamily]
    ipv4_address: str
    ipv6_address: str
    mac_address: str
    state: Port.State
    def __init__(self, name: _Optional[str] = ..., parent: _Optional[str] = ..., owner: _Optional[str] = ..., ip_families: _Optional[_Iterable[_Union[Port.IpFamily, str]]] = ..., ipv4_address: _Optional[str] = ..., ipv6_address: _Optional[str] = ..., mac_address: _Optional[str] = ..., state: _Optional[_Union[Port.State, str]] = ...) -> None: ...

class ListPortsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListPortsResponse(_message.Message):
    __slots__ = ("ports", "next_page_token")
    PORTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ports: _containers.RepeatedCompositeFieldContainer[Port]
    next_page_token: str
    def __init__(self, ports: _Optional[_Iterable[_Union[Port, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetPortRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
