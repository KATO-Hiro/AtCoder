# -*- coding: utf-8 -*-

from enum import Enum, auto


# See:
# https://docs.python.org/ja/3/howto/enum.html
class TwoCirclesPosition(Enum):
    Inside = auto()
    Inscribed = auto()
    Intersect = auto()
    Circumscribed = auto()
    Outside = auto()


def is_intersected(xi: int, yi: int, ri: int, xj: int, yj: int, rj: int):
    dist = abs(xi - xj) ** 2 + abs(yi - yj) ** 2

    if rj > ri:
        ri, rj = rj, ri

    if (ri - rj) ** 2 > dist:
        return TwoCirclesPosition.Inside
    if (ri - rj) ** 2 == dist:
        return TwoCirclesPosition.Inscribed
    elif (ri - rj) ** 2 < dist < (ri + rj) ** 2:
        return TwoCirclesPosition.Intersect
    elif dist == (ri + rj) ** 2:
        return TwoCirclesPosition.Circumscribed
    elif dist > (ri + rj) ** 2:
        return TwoCirclesPosition.Outside


def solve():
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    results = is_intersected(x1, y1, r1, x2, y2, r2)

    if results in [TwoCirclesPosition.Inside, TwoCirclesPosition.Outside]:
        print("No")
    else:
        print("Yes")


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
