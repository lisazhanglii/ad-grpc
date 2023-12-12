from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PostState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    POST_NORMAL: _ClassVar[PostState]
    LOCKED: _ClassVar[PostState]
    POST_HIDDEN: _ClassVar[PostState]
POST_NORMAL: PostState
LOCKED: PostState
POST_HIDDEN: PostState

class Post(_message.Message):
    __slots__ = ("title", "text", "video_url", "image_url", "author", "score", "state", "publication_date")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    VIDEO_URL_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_DATE_FIELD_NUMBER: _ClassVar[int]
    title: str
    text: str
    video_url: str
    image_url: str
    author: str
    score: int
    state: PostState
    publication_date: _timestamp_pb2.Timestamp
    def __init__(self, title: _Optional[str] = ..., text: _Optional[str] = ..., video_url: _Optional[str] = ..., image_url: _Optional[str] = ..., author: _Optional[str] = ..., score: _Optional[int] = ..., state: _Optional[_Union[PostState, str]] = ..., publication_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
