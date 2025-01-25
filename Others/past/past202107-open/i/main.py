# -*- coding: utf-8 -*-

# See:
# https://atcoder.jp/contests/past202107-open/submissions/24377656
from dataclasses import dataclass


@dataclass
class Point:
    x1: int | float
    y1: int | float
    x2: int | float
    y2: int | float

    def __post_init__(self) -> None:
        self.center_x: int | float = (self.x1 + self.x2) / 2
        self.center_y: int | float = (self.y1 + self.y2) / 2

        complex_for_rotation = complex(self.x2 - self.center_x, self.y2 - self.center_y)
        self.unit_vector = complex_for_rotation / abs(complex_for_rotation)

    def rotate(self, x: int | float, y: int | float) -> tuple[int | float, int | float]:
        results = complex(x - self.center_x, y - self.center_y) / self.unit_vector

        return results.real, results.imag


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    point = Point(x1, y1, x2, y2)

    for _ in range(n):
        ai, bi = map(int, input().split())

        print(*point.rotate(ai, bi))


if __name__ == "__main__":
    main()
