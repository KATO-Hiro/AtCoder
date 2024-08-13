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

    size = 10**2  # FIXME: Update value if needs.
    n = int(input())
    cs = []

    for _ in range(n):
        array = [[0 for _ in range(size + 10)] for _ in range(size + 10)]

        for y in range(n):
            ay = list(map(int, input().split()))

            for z, ayz in enumerate(ay):
                array[y][z] = ayz

        c = CumulativeSum2d(array)
        cs.append(c)

    q = int(input())
    ans = list()

    for _ in range(q):
        lxi, rxi, lyi, ryi, lzi, rzi = map(int, input().split())
        candidate = 0

        for x in range(lxi - 1, rxi):
            cx = cs[x]
            candidate += cx.query(lzi - 1, lyi - 1, rzi, ryi)

        ans.append(candidate)

    for ans_i in ans:
        print(ans_i)


if __name__ == "__main__":
    main()
