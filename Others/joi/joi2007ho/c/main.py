# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    xy = set()

    for _ in range(n):
        xi, yi = map(int, input().split())
        xy.add((xi, yi))

    ans = 0

    for i, (xi, yi) in enumerate(xy):
        for j, (xj, yj) in enumerate(xy):
            if i == j:
                continue

            dx = abs(xj - xi)
            dy = abs(yj - yi)

            if (xi + dy, yi + dx) in xy and (xj + dy, yj + dx) in xy:
                ans = max(ans, dx**2 + dy**2)
            elif (xi - dy, yi - dx) in xy and (xj - dy, yj - dx) in xy:
                ans = max(ans, dx**2 + dy**2)

    print(ans)


if __name__ == "__main__":
    main()
