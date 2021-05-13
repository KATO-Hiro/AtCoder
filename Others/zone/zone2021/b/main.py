# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, d, h = map(int, input().split())
    ans = 0

    for i in range(n):
        di, hi = map(int, input().split())

        b = max(0, h - ((h - hi) / (d - di)) * d)
        ans = max(ans, b)

    print(ans)


if __name__ == "__main__":
    main()
