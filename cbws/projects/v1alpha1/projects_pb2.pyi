from cbws.iam.options.v1alpha1 import options_pb2 as _options_pb2
from cbws.iam.policy.v1alpha1 import policy_pb2 as _policy_pb2
from cbws.iam.policy.v1alpha1 import request_response_pb2 as _request_response_pb2
from cbws.projects.v1alpha1 import project_pb2 as _project_pb2
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

class CreateProjectRequest(_message.Message):
    __slots__ = ("parent", "name", "project")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    name: str
    project: _project_pb2.Project
    def __init__(self, parent: _Optional[str] = ..., name: _Optional[str] = ..., project: _Optional[_Union[_project_pb2.Project, _Mapping]] = ...) -> None: ...

class ListProjectsRequest(_message.Message):
    __slots__ = ("page_size", "page_token")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListProjectsResponse(_message.Message):
    __slots__ = ("projects", "next_page_token")
    PROJECTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    projects: _containers.RepeatedCompositeFieldContainer[_project_pb2.Project]
    next_page_token: str
    def __init__(self, projects: _Optional[_Iterable[_Union[_project_pb2.Project, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetProjectRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateProjectRequest(_message.Message):
    __slots__ = ("project", "update_mask")
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    project: _project_pb2.Project
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, project: _Optional[_Union[_project_pb2.Project, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteProjectRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteProjectMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
