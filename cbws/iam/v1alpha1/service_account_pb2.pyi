from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ServiceAccountKeyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SERVICE_ACCOUNT_KEY_TYPE_UNSPECIFIED: _ClassVar[ServiceAccountKeyType]
    SERVICE_ACCOUNT_KEY_TYPE_USER_MANAGED: _ClassVar[ServiceAccountKeyType]
    SERVICE_ACCOUNT_KEY_TYPE_SYSTEM_MANAGED: _ClassVar[ServiceAccountKeyType]

class ServiceAccountKeyAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SERVICE_ACCOUNT_KEY_ALGORITHM_UNSPECIFIED: _ClassVar[ServiceAccountKeyAlgorithm]
    SERVICE_ACCOUNT_KEY_ALGORITHM_RSA_1024: _ClassVar[ServiceAccountKeyAlgorithm]
    SERVICE_ACCOUNT_KEY_ALGORITHM_RSA_2048: _ClassVar[ServiceAccountKeyAlgorithm]
    SERVICE_ACCOUNT_KEY_ALGORITHM_RSA_4096: _ClassVar[ServiceAccountKeyAlgorithm]

class ServiceAccountPrivateKeyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SERVICE_ACCOUNT_PRIVATE_KEY_TYPE_UNSPECIFIED: _ClassVar[ServiceAccountPrivateKeyType]
    SERVICE_ACCOUNT_PRIVATE_KEY_TYPE_CREDENTIALS_FILE: _ClassVar[ServiceAccountPrivateKeyType]
SERVICE_ACCOUNT_KEY_TYPE_UNSPECIFIED: ServiceAccountKeyType
SERVICE_ACCOUNT_KEY_TYPE_USER_MANAGED: ServiceAccountKeyType
SERVICE_ACCOUNT_KEY_TYPE_SYSTEM_MANAGED: ServiceAccountKeyType
SERVICE_ACCOUNT_KEY_ALGORITHM_UNSPECIFIED: ServiceAccountKeyAlgorithm
SERVICE_ACCOUNT_KEY_ALGORITHM_RSA_1024: ServiceAccountKeyAlgorithm
SERVICE_ACCOUNT_KEY_ALGORITHM_RSA_2048: ServiceAccountKeyAlgorithm
SERVICE_ACCOUNT_KEY_ALGORITHM_RSA_4096: ServiceAccountKeyAlgorithm
SERVICE_ACCOUNT_PRIVATE_KEY_TYPE_UNSPECIFIED: ServiceAccountPrivateKeyType
SERVICE_ACCOUNT_PRIVATE_KEY_TYPE_CREDENTIALS_FILE: ServiceAccountPrivateKeyType

class ServiceAccount(_message.Message):
    __slots__ = ("name", "project_id", "unique_id", "email", "display_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    project_id: str
    unique_id: str
    email: str
    display_name: str
    def __init__(self, name: _Optional[str] = ..., project_id: _Optional[str] = ..., unique_id: _Optional[str] = ..., email: _Optional[str] = ..., display_name: _Optional[str] = ...) -> None: ...

class ServiceAccountKey(_message.Message):
    __slots__ = ("name", "key_type", "private_key_type", "key_algorithm", "private_key_data", "public_key_data", "valid_after_time", "valid_before_time")
    NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_TYPE_FIELD_NUMBER: _ClassVar[int]
    KEY_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_DATA_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_DATA_FIELD_NUMBER: _ClassVar[int]
    VALID_AFTER_TIME_FIELD_NUMBER: _ClassVar[int]
    VALID_BEFORE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    key_type: ServiceAccountKeyType
    private_key_type: ServiceAccountPrivateKeyType
    key_algorithm: ServiceAccountKeyAlgorithm
    private_key_data: bytes
    public_key_data: bytes
    valid_after_time: _timestamp_pb2.Timestamp
    valid_before_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., key_type: _Optional[_Union[ServiceAccountKeyType, str]] = ..., private_key_type: _Optional[_Union[ServiceAccountPrivateKeyType, str]] = ..., key_algorithm: _Optional[_Union[ServiceAccountKeyAlgorithm, str]] = ..., private_key_data: _Optional[bytes] = ..., public_key_data: _Optional[bytes] = ..., valid_after_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., valid_before_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
