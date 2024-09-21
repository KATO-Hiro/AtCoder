# -*- coding: utf-8 -*-


from typing import List


class UnionFind:
    """Represents a data structure that tracks a set of elements partitioned
       into a number of disjoint (non-overlapping) subsets.

    Landau notation: O(α(n)), where α(n) is the inverse Ackermann function.

    See:
    https://www.youtube.com/watch?v=zV3Ul2pA2Fw
    https://en.wikipedia.org/wiki/Disjoint-set_data_structure
    https://atcoder.jp/contests/abc120/submissions/4444942
    https://atcoder.jp/contests/abc292/submissions/39410075
    https://github.com/not522/ac-library-python/blob/master/atcoder/dsu.py
    """

    def __init__(self, number_count: int) -> None:
        """
        Args:
            number_count: The size of elements (greater than 2).
        """
        self.number_count = number_count
        self.parent_numbers = [-1 for _ in range(number_count)]
        self.edge_count = [0 for _ in range(number_count)]
        self.group_count = number_count

    def find_root(self, number: int) -> int:
        """Follows the chain of parent pointers from number up the tree until
           it reaches a root element, whose parent is itself.
        Args:
            number: The trees id (0-index).

        Returns:
            The index of a root element.
        """
        if self.parent_numbers[number] < 0:
            return number

        self.parent_numbers[number] = self.find_root(self.parent_numbers[number])
        return self.parent_numbers[number]

    def get_group_size(self, number: int) -> int:
        """
        Args:
            number: The trees id (0-index).

        Returns:
            The size of group.
        """
        return -self.parent_numbers[self.find_root(number)]

    def is_same_group(self, number_x: int, number_y: int) -> bool:
        """Represents the roots of tree number_x and number_y are in the same
           group.
        Args:
            number_x: The trees x (0-index).
            number_y: The trees y (0-index).
        """
        return self.find_root(number_x) == self.find_root(number_y)

    def merge_if_needs(self, number_x: int, number_y: int) -> bool:
        """Uses find_root to determine the roots of the tree number_x and
           number_y belong to. If the roots are distinct, the trees are combined
           by attaching the roots of one to the root of the other.
        Args:
            number_x: The trees x (0-index).
            number_y: The trees y (0-index).
        """
        x = self.find_root(number_x)
        y = self.find_root(number_y)

        self.edge_count[x] += 1

        if x == y:
            return False

        self.group_count -= 1

        if self.parent_numbers[x] > self.parent_numbers[y]:
            x, y = y, x

        self.parent_numbers[x] += self.parent_numbers[y]
        self.parent_numbers[y] = x
        self.edge_count[x] += self.edge_count[y]
        return True

    def get_roots(self) -> List[int]:
        return [i for i, x in enumerate(self.parent_numbers) if x < 0]

    def get_groups(self) -> List[List[int]]:
        roots: List[int] = [self.find_root(i) for i in range(self.number_count)]
        groups: List[List[int]] = [[] for _ in range(self.number_count)]

        for i in range(self.number_count):
            groups[roots[i]].append(i)

        return list(filter(lambda g: g, groups))

    def get_edge_count(self, number: int) -> int:
        return self.edge_count[number]

    def get_group_count(self) -> int:
        return self.group_count


import math
from bisect import bisect_left, bisect_right
from typing import Generic, Iterable, Iterator, List, TypeVar, Union

T = TypeVar("T")


class SortedSet(Generic[T]):
    """Sorted set (set) in C++.

    See:
    https://qiita.com/tatyam/items/492c70ac4c955c055602
    https://github.com/tatyam-prime/SortedSet/blob/main/SortedSet.py
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
        """Make a new SortedSet from iterable.
        / O(N) if sorted and unique / O(N log N)
        """
        a = list(a)

        if not all(a[i] < a[i + 1] for i in range(len(a) - 1)):  # type: ignore
            a = sorted(set(a))  # type: ignore

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
        return "SortedSet" + str(self.a)

    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1 : len(s) - 1] + "}"

    def _find_bucket(self, x: T) -> List[T]:
        "Find the bucket which should contain x. self must not be empty."
        for a in self.a:
            if x <= a[-1]:  # type: ignore
                return a
        return a

    def __contains__(self, x: T) -> bool:
        if self.size == 0:
            return False

        a = self._find_bucket(x)
        i = bisect_left(a, x)  # type: ignore

        return i != len(a) and a[i] == x

    def add(self, x: T) -> bool:
        "Add an element and return True if added. / O(√N)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return True

        a = self._find_bucket(x)
        i = bisect_left(a, x)  # type: ignore

        if i != len(a) and a[i] == x:
            return False

        a.insert(i, x)
        self.size += 1

        if len(a) > len(self.a) * self.REBUILD_RATIO:
            self._build()

        return True

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

    n, q = map(int, input().split())
    uf = UnionFind(n)
    vertices = [SortedSet([i + 1]) for i in range(n)]

    for _ in range(q):
        qi = list(map(int, input().split()))

        if qi[0] == 1:
            u, v = qi[1:]
            u -= 1
            v -= 1

            root_u, root_v = uf.find_root(u), uf.find_root(v)

            if not uf.is_same_group(u, v):
                uf.merge_if_needs(u, v)

            root = uf.find_root(u)

            if root == root_u:
                for vv in vertices[root_v]:
                    vertices[root].add(vv)
            else:
                for vu in vertices[root_u]:
                    vertices[root].add(vu)

            while len(vertices[root]) > 10:
                value_min = vertices[root][0]
                vertices[root].discard(value_min)

        else:
            vi, k = qi[1:]
            vi -= 1

            root_vi = uf.find_root(vi)
            vertices_root = vertices[root_vi]

            if k > len(vertices_root):
                print(-1)
            else:
                print(vertices_root[~(k - 1)])


if __name__ == "__main__":
    main()
