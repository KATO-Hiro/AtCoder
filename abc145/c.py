# -*- coding: utf-8 -*-


def calc_dist(x1, x2, y1, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def main():
    from itertools import permutations

    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    total = 0

    m = len(list(permutations(range(n))))

    for p in permutations(range(n)):
        for i in range(len(p) - 1):
            a = p[i]
            b = p[i + 1]
            total += calc_dist(xy[a][0], xy[b][0], xy[a][1], xy[b][1])

    print(total / m)


if __name__ == '__main__':
    main()
