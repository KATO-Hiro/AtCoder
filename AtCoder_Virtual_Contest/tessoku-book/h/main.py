# -*- coding: utf-8 -*-

from typing import Any, List


# See:
# https://atcoder.jp/contests/abc311/submissions/43843595
class CumulativeSum2d:
    def __init__(self, array: List[List[Any]]) -> None:
        self.height: int = len(array)
        self.width: int = len(array[0])
        self.summed_array: List[List[Any]] = [
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
        assert 0 <= x1 <= x2 <= self.width
        assert 0 <= y1 <= y2 <= self.height

        # x1, y1, x2, y2: 0-indexed
        return (
            self.summed_array[y2][x2]
            - self.summed_array[y1][x2]
            - self.summed_array[y2][x1]
            + self.summed_array[y1][x1]
        )


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    x = [list(map(int, input().split())) for _ in range(h)]
    q = int(input())
    c = CumulativeSum2d(x)

    for _ in range(q):
        ai, bi, ci, di = map(int, input().split())
        print(c.query(bi - 1, ai - 1, di, ci))


if __name__ == "__main__":
    main()
