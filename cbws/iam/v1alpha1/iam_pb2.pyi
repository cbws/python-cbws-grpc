from cbws.iam.options.v1alpha1 import options_pb2 as _options_pb2
from cbws.iam.policy.v1alpha1 import policy_pb2 as _policy_pb2
from cbws.iam.policy.v1alpha1 import request_response_pb2 as _request_response_pb2
from cbws.iam.v1alpha1 import service_account_pb2 as _service_account_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListServiceAccountsRequest(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    def __init__(self, parent: _Optional[str] = ...) -> None: ...

class ListServiceAccountsResponse(_message.Message):
    __slots__ = ("accounts",)
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    accounts: _containers.RepeatedCompositeFieldContainer[_service_account_pb2.ServiceAccount]
    def __init__(self, accounts: _Optional[_Iterable[_Union[_service_account_pb2.ServiceAccount, _Mapping]]] = ...) -> None: ...

class GetServiceAccountRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateServiceAccountRequest(_message.Message):
    __slots__ = ("parent", "account_id", "service_account")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    account_id: str
    service_account: _service_account_pb2.ServiceAccount
    def __init__(self, parent: _Optional[str] = ..., account_id: _Optional[str] = ..., service_account: _Optional[_Union[_service_account_pb2.ServiceAccount, _Mapping]] = ...) -> None: ...

class DeleteServiceAccountRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListServiceAccountKeysRequest(_message.Message):
    __slots__ = ("parent", "key_types")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    KEY_TYPES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    key_types: _containers.RepeatedScalarFieldContainer[_service_account_pb2.ServiceAccountKeyType]
    def __init__(self, parent: _Optional[str] = ..., key_types: _Optional[_Iterable[_Union[_service_account_pb2.ServiceAccountKeyType, str]]] = ...) -> None: ...

class ListServiceAccountKeysResponse(_message.Message):
    __slots__ = ("keys",)
    KEYS_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedCompositeFieldContainer[_service_account_pb2.ServiceAccountKey]
    def __init__(self, keys: _Optional[_Iterable[_Union[_service_account_pb2.ServiceAccountKey, _Mapping]]] = ...) -> None: ...

class GetServiceAccountKeyRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateServiceAccountKeyRequest(_message.Message):
    __slots__ = ("parent", "private_key_type", "key_algorithm")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_TYPE_FIELD_NUMBER: _ClassVar[int]
    KEY_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    parent: str
    private_key_type: _service_account_pb2.ServiceAccountPrivateKeyType
    key_algorithm: _service_account_pb2.ServiceAccountKeyAlgorithm
    def __init__(self, parent: _Optional[str] = ..., private_key_type: _Optional[_Union[_service_account_pb2.ServiceAccountPrivateKeyType, str]] = ..., key_algorithm: _Optional[_Union[_service_account_pb2.ServiceAccountKeyAlgorithm, str]] = ...) -> None: ...

class DeleteServiceAccountKeyRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GenerateAccessTokenRequest(_message.Message):
    __slots__ = ("name", "scope", "lifetime")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    LIFETIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    scope: _containers.RepeatedScalarFieldContainer[str]
    lifetime: _duration_pb2.Duration
    def __init__(self, name: _Optional[str] = ..., scope: _Optional[_Iterable[str]] = ..., lifetime: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class GenerateAccessTokenResponse(_message.Message):
    __slots__ = ("access_token", "expire_time")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    expire_time: _timestamp_pb2.Timestamp
    def __init__(self, access_token: _Optional[str] = ..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
