import sys
from _typeshed import SupportsLenAndGetItem, SupportsRichComparisonT
from collections.abc import Callable, MutableSequence
from typing import TypeVar, overload

_T = TypeVar("_T")

if sys.version_info >= (3, 10):
    @overload
    def bisect_left(
        a: SupportsLenAndGetItem[SupportsRichComparisonT],
        x: SupportsRichComparisonT,
        lo: int = 0,
        hi: int | None = None,
        *,
        key: None = None,
    ) -> int: ...
    @overload
    def bisect_left(
        a: SupportsLenAndGetItem[_T],
        x: SupportsRichComparisonT,
        lo: int = 0,
        hi: int | None = None,
        *,
        key: Callable[[_T], SupportsRichComparisonT],
    ) -> int: ...
    @overload
    def bisect_right(
        a: SupportsLenAndGetItem[SupportsRichComparisonT],
        x: SupportsRichComparisonT,
        lo: int = 0,
        hi: int | None = None,
        *,
        key: None = None,
    ) -> int: ...
    @overload
    def bisect_right(
        a: SupportsLenAndGetItem[_T],
        x: SupportsRichComparisonT,
        lo: int = 0,
        hi: int | None = None,
        *,
        key: Callable[[_T], SupportsRichComparisonT],
    ) -> int: ...
    @overload
    def insort_left(
        a: MutableSequence[SupportsRichComparisonT],
        x: SupportsRichComparisonT,
        lo: int = 0,
        hi: int | None = None,
        *,
        key: None = None,
    ) -> None: ...
    @overload
    def insort_left(
        a: MutableSequence[_T],
        x: _T,
        lo: int = 0,
        hi: int | None = None,
        *,
        key: Callable[[_T], SupportsRichComparisonT],
    ) -> None: ...
    @overload
    def insort_right(
        a: MutableSequence[SupportsRichComparisonT],
        x: SupportsRichComparisonT,
        lo: int = 0,
        hi: int | None = None,
        *,
        key: None = None,
    ) -> None: ...
    @overload
    def insort_right(
        a: MutableSequence[_T],
        x: _T,
        lo: int = 0,
        hi: int | None = None,
        *,
        key: Callable[[_T], SupportsRichComparisonT],
    ) -> None: ...

else:
    def bisect_left(
        a: SupportsLenAndGetItem[SupportsRichComparisonT],
        x: SupportsRichComparisonT,
        lo: int = 0,
        hi: int | None = None,
    ) -> int: ...
    def bisect_right(
        a: SupportsLenAndGetItem[SupportsRichComparisonT],
        x: SupportsRichComparisonT,
        lo: int = 0,
        hi: int | None = None,
    ) -> int: ...
    def insort_left(
        a: MutableSequence[SupportsRichComparisonT],
        x: SupportsRichComparisonT,
        lo: int = 0,
        hi: int | None = None,
    ) -> None: ...
    def insort_right(
        a: MutableSequence[SupportsRichComparisonT],
        x: SupportsRichComparisonT,
        lo: int = 0,
        hi: int | None = None,
    ) -> None: ...
