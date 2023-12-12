from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommentState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMMENT_NORMAL: _ClassVar[CommentState]
    COMMENT_HIDDEN: _ClassVar[CommentState]
COMMENT_NORMAL: CommentState
COMMENT_HIDDEN: CommentState

class Comment(_message.Message):
    __slots__ = ("author", "text", "score", "state", "publication_date")
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_DATE_FIELD_NUMBER: _ClassVar[int]
    author: str
    text: str
    score: int
    state: CommentState
    publication_date: _timestamp_pb2.Timestamp
    def __init__(self, author: _Optional[str] = ..., text: _Optional[str] = ..., score: _Optional[int] = ..., state: _Optional[_Union[CommentState, str]] = ..., publication_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
