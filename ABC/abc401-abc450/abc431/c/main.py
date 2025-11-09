# -*- coding: utf-8 -*-


import math
from bisect import bisect_left, bisect_right, insort
from typing import Generic, Iterable, Iterator, List, TypeVar, Union

T = TypeVar("T")


class SortedMultiset(Generic[T]):
    """Sorted multi set (set) in C++.

    See:
    https://qiita.com/tatyam/items/492c70ac4c955c055602
    https://github.com/tatyam-prime/SortedSet/blob/main/SortedMultiset.py
    """

    BUCKET_RATIO = 50
    REBUILD_RATIO = 170

    def _build(self, a=None) -> None:
        "Evenly divide `a` into buckets."
        if a is None:
            a = list(self)

        size = self.size = len(a)
        bucket_size = int(math.ceil(math.sqrt(size / self.BUCKET_RATIO)))
        self.a = [
            a[size * i // bucket_size : size * (i + 1) // bucket_size]
            for i in range(bucket_size)
        ]

    def __init__(self, a: Iterable[T] = []) -> None:
        "Make a new SortedMultiset from iterable. / O(N) if sorted / O(N log N)"
        a = list(a)

        if not all(a[i] <= a[i + 1] for i in range(len(a) - 1)):  # type: ignore
            a = sorted(a)  # type: ignore

        self._build(a)

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i:
                yield j  # type: ignore

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i):
                yield j

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return "SortedMultiset" + str(self.a)

    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1 : len(s) - 1] + "}"

    def _find_bucket(self, x: T) -> List[T]:
        "Find the bucket which should contain x. self must not be empty."
        for a in self.a:
            if x <= a[-1]:  # type: ignore
                return a
        return a  # type: ignore

    def __contains__(self, x: T) -> bool:
        if self.size == 0:
            return False

        a = self._find_bucket(x)
        i = bisect_left(a, x)  # type: ignore
        return i != len(a) and a[i] == x

    def count(self, x: T) -> int:
        "Count the number of x."
        return self.index_right(x) - self.index(x)

    def add(self, x: T) -> None:
        "Add an element. / O(√N)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return

        a = self._find_bucket(x)
        insort(a, x)  # type: ignore
        self.size += 1

        if len(a) > len(self.a) * self.REBUILD_RATIO:
            self._build()

    def discard(self, x: T) -> bool:
        "Remove an element and return True if removed. / O(√N)"
        if self.size == 0:
            return False

        a = self._find_bucket(x)
        i = bisect_left(a, x)  # type: ignore

        if i == len(a) or a[i] != x:
            return False

        a.pop(i)
        self.size -= 1

        if len(a) == 0:
            self._build()

        return True

    def lt(self, x: T) -> Union[T, None]:
        "Find the largest element < x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] < x:  # type: ignore
                return a[bisect_left(a, x) - 1]  # type: ignore
        return None

    def le(self, x: T) -> Union[T, None]:
        "Find the largest element <= x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] <= x:  # type: ignore
                return a[bisect_right(a, x) - 1]  # type: ignore
        return None

    def gt(self, x: T) -> Union[T, None]:
        "Find the smallest element > x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] > x:  # type: ignore
                return a[bisect_right(a, x)]  # type: ignore
        return None

    def ge(self, x: T) -> Union[T, None]:
        "Find the smallest element >= x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] >= x:  # type: ignore
                return a[bisect_left(a, x)]  # type: ignore
        return None

    def __getitem__(self, x: int) -> T:
        "Return the x-th element, or IndexError if it doesn't exist."
        if x < 0:
            x += self.size
        if x < 0:
            raise IndexError

        for a in self.a:
            if x < len(a):
                return a[x]  # type: ignore

            x -= len(a)
        raise IndexError

    def index(self, x: T) -> int:
        "Count the number of elements < x."
        ans = 0

        for a in self.a:
            if a[-1] >= x:  # type: ignore
                return ans + bisect_left(a, x)  # type: ignore
            ans += len(a)
        return ans

    def index_right(self, x: T) -> int:
        "Count the number of elements <= x."
        ans = 0

        for a in self.a:
            if a[-1] > x:  # type: ignore
                return ans + bisect_right(a, x)  # type: ignore
            ans += len(a)
        return ans


def main():
    import sys

    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    h = sorted(map(int, input().split()))
    b = list(map(int, input().split()))
    st = SortedMultiset(b)
    count = 0

    for hi in h:
        value = st.ge(hi)

        if value is None:
            break

        st.discard(value)
        count += 1

    if count >= k:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
