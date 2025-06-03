# -*- coding: utf-8 -*-


def solve():
    n = int(input())
    s = input().rstrip()

    inf = 10**18
    dp = [0] * 3

    for si in s:
        ndp = [inf] * 3
        si = int(si)

        ndp[0] = min(ndp[0], dp[0] + (0 ^ si))
        ndp[1] = min(ndp[1], dp[0] + (1 ^ si), dp[1] + (1 ^ si))
        ndp[2] = min(ndp[2], dp[0] + (0 ^ si), dp[1] + (0 ^ si), dp[2] + (0 ^ si))

        dp = ndp

    print(min(dp))


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
