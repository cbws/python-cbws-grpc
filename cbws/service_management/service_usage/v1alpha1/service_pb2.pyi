from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LaunchStage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LAUNCH_STAGE_UNSPECIFIED: _ClassVar[LaunchStage]
    LAUNCH_STAGE_PRIVATE_PREVIEW: _ClassVar[LaunchStage]
    LAUNCH_STAGE_PREVIEW: _ClassVar[LaunchStage]
    LAUNCH_STAGE_GA: _ClassVar[LaunchStage]

class ServiceState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SERVICE_STATE_UNSPECIFIED: _ClassVar[ServiceState]
    SERVICE_STATE_DISABLED: _ClassVar[ServiceState]
    SERVICE_STATE_ENABLED: _ClassVar[ServiceState]
LAUNCH_STAGE_UNSPECIFIED: LaunchStage
LAUNCH_STAGE_PRIVATE_PREVIEW: LaunchStage
LAUNCH_STAGE_PREVIEW: LaunchStage
LAUNCH_STAGE_GA: LaunchStage
SERVICE_STATE_UNSPECIFIED: ServiceState
SERVICE_STATE_DISABLED: ServiceState
SERVICE_STATE_ENABLED: ServiceState

class Service(_message.Message):
    __slots__ = ("name", "parent", "config", "state")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    parent: str
    config: ServiceConfig
    state: ServiceState
    def __init__(self, name: _Optional[str] = ..., parent: _Optional[str] = ..., config: _Optional[_Union[ServiceConfig, _Mapping]] = ..., state: _Optional[_Union[ServiceState, str]] = ...) -> None: ...

class ServiceConfig(_message.Message):
    __slots__ = ("name", "title", "launch_stage", "description", "metrics", "quota")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_STAGE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    QUOTA_FIELD_NUMBER: _ClassVar[int]
    name: str
    title: str
    launch_stage: LaunchStage
    description: str
    metrics: _containers.RepeatedCompositeFieldContainer[Metric]
    quota: Quota
    def __init__(self, name: _Optional[str] = ..., title: _Optional[str] = ..., launch_stage: _Optional[_Union[LaunchStage, str]] = ..., description: _Optional[str] = ..., metrics: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., quota: _Optional[_Union[Quota, _Mapping]] = ...) -> None: ...

class Metric(_message.Message):
    __slots__ = ("name", "display_name", "unit", "billed")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    BILLED_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    unit: str
    billed: bool
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., unit: _Optional[str] = ..., billed: bool = ...) -> None: ...

class Quota(_message.Message):
    __slots__ = ("metric_rules", "limits")
    METRIC_RULES_FIELD_NUMBER: _ClassVar[int]
    LIMITS_FIELD_NUMBER: _ClassVar[int]
    metric_rules: _containers.RepeatedCompositeFieldContainer[MetricRule]
    limits: _containers.RepeatedCompositeFieldContainer[QuotaLimit]
    def __init__(self, metric_rules: _Optional[_Iterable[_Union[MetricRule, _Mapping]]] = ..., limits: _Optional[_Iterable[_Union[QuotaLimit, _Mapping]]] = ...) -> None: ...

class MetricRule(_message.Message):
    __slots__ = ("selector", "metric_costs")
    class MetricCostsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    SELECTOR_FIELD_NUMBER: _ClassVar[int]
    METRIC_COSTS_FIELD_NUMBER: _ClassVar[int]
    selector: str
    metric_costs: _containers.ScalarMap[str, int]
    def __init__(self, selector: _Optional[str] = ..., metric_costs: _Optional[_Mapping[str, int]] = ...) -> None: ...

class QuotaLimit(_message.Message):
    __slots__ = ("metric", "default_limit", "duration")
    METRIC_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    metric: str
    default_limit: int
    duration: _duration_pb2.Duration
    def __init__(self, metric: _Optional[str] = ..., default_limit: _Optional[int] = ..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
