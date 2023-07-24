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
        return (
            self.summed_array[y2][x2]
            - self.summed_array[y1][x2]
            - self.summed_array[y2][x1]
            + self.summed_array[y1][x1]
        )


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    size = 10**3
    c = [[0 for _ in range(size + 10)] for _ in range(size + 10)]

    for _ in range(n):
        lxi, lyi, rxi, ryi = map(int, input().split())
        c[lyi][lxi] += 1
        c[lyi][rxi] -= 1
        c[ryi][lxi] -= 1
        c[ryi][rxi] += 1

    d = CumulativeSum2d(c)
    count = defaultdict(int)

    for i in range(size + 1):
        for j in range(size + 1):
            count[d.summed_array[i][j]] += 1

    for i in range(1, n + 1):
        print(count[i])


if __name__ == "__main__":
    main()
