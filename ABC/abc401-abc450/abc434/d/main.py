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

    n = int(input())
    udlr = [tuple(map(int, input().split())) for _ in range(n)]

    size = 2 * 10**3  # FIXME: Update value if needs.
    array = [[0 for _ in range(size + 10)] for _ in range(size + 10)]

    for ui, di, li, ri in udlr:
        array[ui - 1][li - 1] += 1
        array[ui - 1][ri] -= 1
        array[di][li - 1] -= 1
        array[di][ri] += 1

    c = CumulativeSum2d(array)
    counts = c.get_summed_array()
    total = (2 * 10**3) ** 2
    ones = [[0 for _ in range(size + 10)] for _ in range(size + 10)]

    for i in range(size + 1):
        for j in range(size + 1):
            count = counts[i][j]

            if count <= 0:
                continue

            total -= 1

            if count == 1:
                ones[i][j] = 1

    c_ones = CumulativeSum2d(ones)

    for ui, di, li, ri in udlr:
        cur = c_ones.query(li, ui, ri + 1, di + 1)
        ans = total + cur
        print(ans)


if __name__ == "__main__":
    main()
