# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    x = [0 for _ in range(n)]
    y = [0 for _ in range(n)]

    for i in range(n):
        xi, yi = map(int, input().split())
        x[i] = xi + yi
        y[i] = xi - yi

    ans = max(x) - min(x)
    ans = max(ans, max(y) - min(y))

    print(ans)


if __name__ == "__main__":
    main()
