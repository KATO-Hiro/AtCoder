# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    inf = 10**18
    dp = [-inf] * 2
    dp[0] = 0

    for ai in a:
        ndp = [0] * 2
        ndp[0] = max(ndp[0], dp[0], dp[1])
        ndp[1] = max(ndp[1], dp[0] + ai, dp[1] + ai - k)

        dp = ndp

    print(max(dp))


if __name__ == "__main__":
    main()
