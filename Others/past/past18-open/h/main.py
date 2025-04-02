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
        # x1, y1, x2, y2: 0-indexed
        assert 0 <= x1 <= x2 <= self.width
        assert 0 <= y1 <= y2 <= self.height

        return (
            self.summed_array[y2][x2]
            - self.summed_array[y1][x2]
            - self.summed_array[y2][x1]
            + self.summed_array[y1][x1]
        )

    def get_summed_array(self) -> List[List[Any]]:
        return self.summed_array


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    # 2次元累積和
    size = n  # FIXME: Update value if needs.
    array = [[0 for _ in range(size + 10)] for _ in range(size + 10)]

    for i in range(n):
        si = input().rstrip()

        for j, sij in enumerate(si):
            if sij == ".":
                continue

            array[i][j] += 1

    c = CumulativeSum2d(array)
    ans = 0

    # 左上の座標(i, j)とlevelを決め打ち
    # 矩形領域に分割
    # 内側の領域: #0個、全体: 3 * level + 4
    for i in range(n):
        for j in range(n):
            for size in range(2, n):
                ni, nj = i + size, j + size

                if ni >= n or nj >= n:
                    break

                ok = True
                inner_count = c.query(j + 1, i + 1, nj + 1, ni)

                if inner_count != 0:
                    ok = False

                outer_count = c.query(j, i, nj + 1, ni + 1)
                level = size - 1

                if outer_count != 3 * level + 4:
                    ok = False

                if ok:
                    ans = max(ans, level)

    print(ans)


if __name__ == "__main__":
    main()
