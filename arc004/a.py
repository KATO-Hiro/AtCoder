# -*- coding: utf-8 -*-


def main():
    from math import sqrt
    from itertools import combinations

    n = int(input())
    xy = list()

    for i in range(n):
        xy.append(tuple(map(int, input().split())))

    ans = 0

    for point1, point2 in list(combinations(xy, 2)):
        dist = sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)
        ans = max(ans, dist)

    print(ans)


if __name__ == '__main__':
    main()
