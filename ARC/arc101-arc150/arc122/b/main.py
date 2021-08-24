# -*- coding: utf-8 -*-


def main():
    from statistics import median
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    x = median(a) / 2

    for ai in a:
        ans += x + ai - min(ai, 2 * x)

    print(ans / n)


if __name__ == "__main__":
    main()
