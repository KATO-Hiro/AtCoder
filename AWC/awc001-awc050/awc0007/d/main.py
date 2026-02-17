# -*- coding: utf-8 -*-

from typing import Any


# See:
# https://atcoder.jp/contests/abc311/submissions/43843595
class CumulativeSum2d:
    def __init__(self, array: list[list[Any]]) -> None:
        self.height: int = len(array)
        self.width: int = len(array[0])
        self.summed_array: list[list[Any]] = [
            [0] * (self.width + 1) for _ in range(self.height + 1)
        ]

        for i in range(self.height):
            for j in range(self.width):
                self.summed_array[i + 1][j + 1] = (
                    self.summed_array[i + 1][j]
                    + self.summed_array[i][j + 1]
                    - self.summed_array[i][j]
                    + array[i][j]
                )

    def query(self, x1: int, y1: int, x2: int, y2: int) -> Any:
        # x1, y1, x2, y2: 0-indexed
        assert 0 <= x1 <= x2 <= self.width
        assert 0 <= y1 <= y2 <= self.height

        return (
            self.summed_array[y2][x2]
            - self.summed_array[y1][x2]
            - self.summed_array[y2][x1]
            + self.summed_array[y1][x1]
        )

    def get_summed_array(self) -> list[list[Any]]:
        return self.summed_array


def main():
    import sys

    input = sys.stdin.readline

    n, a, b = map(int, input().split())
    size = n  # FIXME: Update value if needs.
    array1 = [[0 for _ in range(size + 10)] for _ in range(size + 10)]
    array2 = [[0 for _ in range(size + 10)] for _ in range(size + 10)]

    for _ in range(a):
        x1, y1, x2, y2 = map(int, input().split())

        # 0-indexed.
        y1 -= 1
        x1 -= 1

        array1[y1][x1] += 1
        array1[y1][x2] -= 1
        array1[y2][x1] -= 1
        array1[y2][x2] += 1

    c1 = CumulativeSum2d(array1)
    results1 = c1.get_summed_array()

    for _ in range(b):
        x1, y1, x2, y2 = map(int, input().split())

        # 0-indexed.
        y1 -= 1
        x1 -= 1

        array2[y1][x1] += 1
        array2[y1][x2] -= 1
        array2[y2][x1] -= 1
        array2[y2][x2] += 1

    c2 = CumulativeSum2d(array2)
    results2 = c2.get_summed_array()

    ans = 0

    for i in range(size + 1):
        for j in range(size + 1):
            if results1[i][j] >= 1 and results2[i][j] >= 1:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
