from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Subreddit(_message.Message):
    __slots__ = ("name", "visibility", "tags")
    class Visibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PUBLIC: _ClassVar[Subreddit.Visibility]
        PRIVATE: _ClassVar[Subreddit.Visibility]
        HIDDEN: _ClassVar[Subreddit.Visibility]
    PUBLIC: Subreddit.Visibility
    PRIVATE: Subreddit.Visibility
    HIDDEN: Subreddit.Visibility
    NAME_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    visibility: Subreddit.Visibility
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., visibility: _Optional[_Union[Subreddit.Visibility, str]] = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...
