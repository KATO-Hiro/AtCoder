# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, n = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    inf = 10 ** 18
    dp = [inf] * (h + 1)
    dp[h] = 0

    for hi in range(h, 0, -1):
        for ai, bi in ab:
            diff = max(0, hi - ai)
            dp[diff] = min(dp[diff], dp[hi] + bi)

    print(dp[0])


if __name__ == "__main__":
    main()
