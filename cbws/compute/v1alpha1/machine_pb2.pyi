from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Machine(_message.Message):
    __slots__ = ("name", "parent", "type", "image", "hostname", "address", "ipv6_address", "ssh_keys", "userdata", "service_account", "state")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Machine.State]
        STATE_PROVISIONING: _ClassVar[Machine.State]
        STATE_STAGING: _ClassVar[Machine.State]
        STATE_RUNNING: _ClassVar[Machine.State]
        STATE_STOPPING: _ClassVar[Machine.State]
        STATE_SUSPENDING: _ClassVar[Machine.State]
        STATE_SUSPENDED: _ClassVar[Machine.State]
        STATE_REPAIRING: _ClassVar[Machine.State]
        STATE_TERMINATED: _ClassVar[Machine.State]
    STATE_UNSPECIFIED: Machine.State
    STATE_PROVISIONING: Machine.State
    STATE_STAGING: Machine.State
    STATE_RUNNING: Machine.State
    STATE_STOPPING: Machine.State
    STATE_SUSPENDING: Machine.State
    STATE_SUSPENDED: Machine.State
    STATE_REPAIRING: Machine.State
    STATE_TERMINATED: Machine.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    IPV6_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SSH_KEYS_FIELD_NUMBER: _ClassVar[int]
    USERDATA_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    parent: str
    type: str
    image: str
    hostname: str
    address: str
    ipv6_address: str
    ssh_keys: _containers.RepeatedScalarFieldContainer[str]
    userdata: str
    service_account: str
    state: Machine.State
    def __init__(self, name: _Optional[str] = ..., parent: _Optional[str] = ..., type: _Optional[str] = ..., image: _Optional[str] = ..., hostname: _Optional[str] = ..., address: _Optional[str] = ..., ipv6_address: _Optional[str] = ..., ssh_keys: _Optional[_Iterable[str]] = ..., userdata: _Optional[str] = ..., service_account: _Optional[str] = ..., state: _Optional[_Union[Machine.State, str]] = ...) -> None: ...
