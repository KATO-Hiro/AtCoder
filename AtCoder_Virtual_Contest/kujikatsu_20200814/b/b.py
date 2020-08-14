# -*- coding: utf-8 -*-


def main():
    from itertools import permutations
    from math import sqrt

    n = int(input())
    x = [0 for _ in range(n)]
    y = [0 for _ in range(n)]

    for i in range(n):
        xi, yi = map(int, input().split())
        x[i] = xi
        y[i] = yi

    path = list(permutations(range(n)))
    path_count = len(path)
    length = 0

    for p in path:
        for i, j in zip(p, p[1:]):
            length += sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)

    print(length / path_count)


if __name__ == '__main__':
    main()
