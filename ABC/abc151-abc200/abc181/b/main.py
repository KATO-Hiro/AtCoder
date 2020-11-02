# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate

    import sys

    input = sys.stdin.readline

    n = int(input())
    summed = list(accumulate([i for i in range(10 ** 6 + 10)]))
    ans = 0

    for i in range(n):
        ai, bi = map(int, input().split())
        ans += summed[bi] - summed[ai - 1]

    print(ans)


if __name__ == "__main__":
    main()
