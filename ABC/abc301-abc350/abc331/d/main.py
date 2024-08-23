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

    n, q = map(int, input().split())
    grid = [[0] * n for _ in range(n)]

    # 黒マスを1として、二次元累積和で個数を前計算
    for i in range(n):
        pi = input().rstrip()

        for j, pij in enumerate(pi):
            if pij == "B":
                grid[i][j] = 1

    c = CumulativeSum2d(grid)

    # 長方形の領域を4分割
    def f(y, x):
        py, qy = divmod(y, n)
        px, qx = divmod(x, n)

        count = px * py * c.query(0, 0, n, n)
        count += py * c.query(0, 0, qx, n)
        count += px * c.query(0, 0, n, qy)
        count += c.query(0, 0, qx, qy)

        return count

    for _ in range(q):
        ai, bi, ci, di = map(int, input().split())
        ci += 1
        di += 1

        ans = f(ci, di) - f(ci, bi) - f(ai, di) + f(ai, bi)
        print(ans)


if __name__ == "__main__":
    main()
