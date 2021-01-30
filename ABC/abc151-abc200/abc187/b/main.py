# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    xy = list()

    for i in range(n):
        xi, yi = map(int, input().split())
        xy.append((xi, yi))

    ans = 0

    for i in range(n):
        xi, yi = xy[i]

        for j in range(i + 1, n):
            xj, yj = xy[j]

            if abs(yj - yi) <= abs(xj - xi):
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
