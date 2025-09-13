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

    n, q = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(n)]

    size = 5 * 10**2  # FIXME: Update value if needs.
    array = [[0 for _ in range(size + 10)] for _ in range(size + 10)]

    # 2 * 2 の白マスが置けるか判定し、その場合は左上に置く
    for i in range(n):
        for j in range(n):
            if i + 1 >= n or j + 1 >= n:
                continue
            if (
                s[i][j] == "#"
                or s[i][j + 1] == "#"
                or s[i + 1][j] == "#"
                or s[i + 1][j + 1] == "#"
            ):
                continue

            array[i][j] += 1

    c = CumulativeSum2d(array)

    for _ in range(q):
        ui, di, li, ri = map(int, input().split())
        ans = c.query(li - 1, ui - 1, ri - 1, di - 1)
        print(ans)


if __name__ == "__main__":
    main()
