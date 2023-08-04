# -*- coding: utf-8 -*-

from typing import Tuple


# 3頂点から面積を求める
# See:
# https://mathwords.net/x1y2hikux2y1
def calc_area_of_triangle(
    point1: Tuple[int, int], point2: Tuple[int, int], point3: Tuple[int, int]
):
    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3

    area = abs((x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3)) / 2

    return area


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    xy = [tuple(map(int, input().split())) for _ in range(n)]
    ans = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                result = calc_area_of_triangle(xy[i], xy[j], xy[k])

                if result > 0.0:
                    ans += 1

    print(ans)


if __name__ == "__main__":
    main()
