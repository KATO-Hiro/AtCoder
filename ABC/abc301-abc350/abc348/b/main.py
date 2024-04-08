# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    xy = [tuple(map(int, input().split())) for _ in range(n)]

    for i, (xi, yi) in enumerate(xy, 1):
        dist = list()

        for j, (xj, yj) in enumerate(xy, 1):
            if i == j:
                continue

            d = (xi - xj) ** 2 + (yi - yj) ** 2
            dist.append((d, j))

        dist = sorted(dist, key=lambda x: (-x[0], x[1]))
        print(dist[0][1])


if __name__ == "__main__":
    main()
