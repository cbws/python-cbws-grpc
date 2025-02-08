from cbws.iam.policy.v1alpha1 import policy_pb2 as _policy_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetPolicyRequest(_message.Message):
    __slots__ = ("resource", "policy")
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    resource: str
    policy: _policy_pb2.Policy
    def __init__(self, resource: _Optional[str] = ..., policy: _Optional[_Union[_policy_pb2.Policy, _Mapping]] = ...) -> None: ...

class GetPolicyRequest(_message.Message):
    __slots__ = ("resource",)
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    resource: str
    def __init__(self, resource: _Optional[str] = ...) -> None: ...

class TestPermissionsRequest(_message.Message):
    __slots__ = ("resource", "permissions")
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    resource: str
    permissions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, resource: _Optional[str] = ..., permissions: _Optional[_Iterable[str]] = ...) -> None: ...

class TestPermissionsResponse(_message.Message):
    __slots__ = ("permissions",)
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, permissions: _Optional[_Iterable[str]] = ...) -> None: ...
