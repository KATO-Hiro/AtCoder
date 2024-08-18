# -*- coding: utf-8 -*-

# See:
# Original source: https://atcoder.jp/contests/abc367/submissions/56800083
# Translate C++ to Python

from bisect import bisect_left, bisect_right
from typing import Generic, List, TypeVar

T = TypeVar("T", bound=List[int])

NOT_FOUND = -1


class Finder(Generic[T]):
    def __init__(self, values: T = [], offset: int = 0) -> None:
        self.values = values
        self.offset = offset
        self.indexes = []

        if values:
            self.init(values, offset)

    def init(self, values: T, offset: int = 0) -> None:
        self.values = values
        self.offset = offset

        if not self.values:
            return None

        value_min, value_max = min(values), max(values)
        inf = offset + 10**12
        assert offset <= value_min and value_max < inf
        self.indexes = [[] for _ in range(value_max - offset + 1)]

        for i in range(len(self.values)):
            self.find_indexes(self.values[i]).append(i)

    def append_list(self, values: T) -> None:
        for value in values:
            self.append(value)

    def append(self, value: int) -> None:
        assert self.offset <= value

        if len(self.indexes) <= value - self.offset:
            self.indexes.extend(
                [[] for _ in range(value - self.offset - len(self.indexes) + 1)]
            )
        self.find_indexes(value).append(self.get_size())
        self.values.append(value)

    def pop(self) -> int | None:
        if self.is_empty():
            return None

        self.find_indexes(self.values[-1]).pop()

        return self.values.pop()

    def clear(self) -> None:
        self.values.clear()
        self.indexes.clear()

    def find_indexes(self, value: int) -> List[int]:
        if self._validate_range(value):
            return [NOT_FOUND]

        return self.indexes[value - self.offset]

    def find_index(self, value: int, right: int) -> int:
        if self._validate_range(value):
            return NOT_FOUND

        indexes = self.find_indexes(value)

        return NOT_FOUND if len(indexes) <= right else indexes[right]

    def find_next_index(self, index: int, value: int) -> int:
        if self._validate_range(value):
            return NOT_FOUND

        indexes = self.find_indexes(value)
        pos = bisect_right(indexes, index)

        return NOT_FOUND if pos == len(indexes) else indexes[pos]

    def find_prev_index(self, index: int, value: int) -> int:
        if self._validate_range(value):
            return NOT_FOUND

        indexes = self.find_indexes(value)
        pos = bisect_left(indexes, index)

        return NOT_FOUND if pos == 0 else indexes[pos - 1]

    def find_ceil_index(self, index: int, value: int) -> int:
        return self.find_next_index(index - 1, value)

    def find_floor_index(self, index: int, value: int) -> int:
        return self.find_prev_index(index + 1, value)

    def find_cycle_next_index(self, index: int, value: int) -> int:
        if self._validate_range(value):
            return NOT_FOUND

        next_index = self.find_next_index(index, value)

        if next_index == NOT_FOUND:
            next_index = self.find_next_index(-1, value)

        return next_index

    def find_cycle_prev_index(self, index: int, value: int) -> int:
        if self._validate_range(value):
            return NOT_FOUND

        prev_index = self.find_prev_index(index, value)

        if prev_index == NOT_FOUND:
            prev_index = self.find_prev_index(self.get_size(), value)

        return prev_index

    def find_cycle_ceil_index(self, index: int, value: int) -> int:
        return self.find_cycle_next_index(index - 1, value)

    def find_cycle_floor_index(self, index: int, value: int) -> int:
        return self.find_cycle_prev_index(index + 1, value)

    def count_values_in_ranges(self, value: int, left: int, right: int) -> int:
        return self._count_value(right, value) - self._count_value(left - 1, value)

    def is_empty(self) -> bool:
        return not self.values

    def get_size(self) -> int:
        return len(self.values)

    def _validate_range(self, value: int) -> bool:
        return value < self.offset or self.offset + len(self.indexes) <= value

    def _count_value(self, right: int, value: int) -> int:
        if self._validate_range(value):
            return 0

        indexes = self.find_indexes(value)

        return bisect_right(indexes, right)


def main():
    import sys
    from collections import defaultdict
    from itertools import accumulate

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    acc = list(accumulate(a + a, initial=0))
    d = defaultdict(int)

    # 数列がmの倍数 => mod mの頻度を数える
    b = [acc_i % m for acc_i in acc]
    f = Finder(b)
    ans = 0

    # 区間[j + 1, j + n - 1]の範囲に含まれるb[j]の個数を数える
    for j in range(n):
        count = f.count_values_in_ranges(b[j], j + 1, j + n - 1)
        ans += count

    print(ans)


if __name__ == "__main__":
    main()
