# -*- coding: utf-8 -*-


def solve():
    n = int(input())
    s = input().rstrip()

    inf = 10**18
    dp = [[inf] * 2 for _ in range(2)]
    dp[0][0] = 0

    for si in s:
        ndp = [[inf] * 2 for _ in range(2)]
        si = int(si)

        ndp[0][0] = min(ndp[0][0], dp[0][0] + (0 ^ si))
        ndp[1][1] = min(ndp[1][1], dp[0][0] + (1 ^ si))
        ndp[0][1] = min(ndp[0][1], dp[0][1] + (0 ^ si))
        ndp[1][1] = min(ndp[1][1], dp[1][1] + (1 ^ si))
        ndp[0][1] = min(ndp[0][1], dp[1][1] + (0 ^ si))

        dp = ndp

    print(min(dp[0][0], dp[0][1], dp[1][0], dp[1][1]))


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
