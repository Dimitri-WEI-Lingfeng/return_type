from typing import *

from return_type import ReturnType
from collections import abc

v_int: ReturnType[Callable[..., int]] = 1
v_float: ReturnType[Callable[..., float]] = 1.1
v_str: ReturnType[Callable[..., str]] = "123"
v_bytes: ReturnType[Callable[..., bytes]] = b"2123"
v_hash: ReturnType[Callable[..., Hashable]] = 1


class AwaitableClass(Awaitable[Any]):
    def __await__(self):
        pass


v_awaitable: ReturnType[Callable[..., Awaitable[Any]]] = AwaitableClass()


async def cof() -> Any:
    pass


v_coroutine: ReturnType[Callable[..., Coroutine]] = cof()

# TODO add test for types below
# AsyncIterable,
# AsyncIterator,
# Iterable,
# Iterator,
# Reversible,
# Sized,
# Container,
# Collection,
# Callable,
# AbstractSet,
# MutableSet,
# # NOTE: Mapping is only covariant in the value type.
# Mapping,
# MutableMapping,
# Sequence,
# MutableSequence,
# ByteString,
# # Tuple accepts variable number of parameters.
# Tuple,
# List,
# Deque,
# Set,
# FrozenSet,
# MappingView,
# KeysView,
# ItemsView,
# ValuesView,
# ContextManager,
# AsyncContextManager,
# Dict,
# DefaultDict,
# OrderedDict,
# Counter,
# ChainMap,
# Generator,
# AsyncGenerator,
# TypedDict,
