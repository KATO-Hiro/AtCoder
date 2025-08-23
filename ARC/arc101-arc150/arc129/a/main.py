# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, l, r = map(int, input().split())

    total = 0

    for i in range(60, -1, -1):
        if (n >> i) & 1:
            lower = max(2**i, l)
            upper = min(2 ** (i + 1) - 1, r)
            total += max(0, upper - lower + 1)

    print(total)


if __name__ == "__main__":
    main()
