# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    xy = [tuple(map(int, input().split())) for _ in range(n)]
    ans = 0

    for j, (xj, yj) in enumerate(xy):
        dist_min = float("inf")

        for ai in a:
            ai -= 1
            xi, yi = xy[ai]

            dist = (xi - xj) ** 2 + (yi - yj) ** 2
            dist_min = min(dist_min, dist)

        ans = max(ans, dist_min)

    print(ans**0.5)


if __name__ == "__main__":
    main()
