from typing import *
import pytest

from return_type import ReturnType


def test_correct_input():
    T = TypeVar("T")
    for tp in (
        T,
        int,
        float,
        str,
        bytes,
        Hashable,
        Awaitable,
        Coroutine,
        AsyncIterable,
        AsyncIterator,
        Iterable,
        Iterator,
        Reversible,
        Sized,
        Container,
        Collection,
        Callable,
        AbstractSet,
        MutableSet,
        # NOTE: Mapping is only covariant in the value type.
        Mapping,
        MutableMapping,
        Sequence,
        MutableSequence,
        ByteString,
        # Tuple accepts variable number of parameters.
        Tuple,
        List,
        Deque,
        Set,
        FrozenSet,
        MappingView,
        KeysView,
        ItemsView,
        ValuesView,
        ContextManager,
        AsyncContextManager,
        Dict,
        DefaultDict,
        OrderedDict,
        Counter,
        ChainMap,
        Generator,
        AsyncGenerator,
        TypedDict,
    ):
        assert ReturnType[Callable[..., tp]] is tp

    assert ReturnType[Callable[..., None]] is type(None)


def test_pass_non_callable_type():
    with pytest.raises(TypeError):
        T = ReturnType[int]


def test_pass_built_in_callable_type():
    with pytest.raises(TypeError):
        T = ReturnType[Callable]
