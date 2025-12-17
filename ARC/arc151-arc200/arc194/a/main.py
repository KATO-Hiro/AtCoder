# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    inf = 10**18
    dp = [-inf] * 2
    dp[0] = 0

    for ai in a:
        ndp = [-inf] * 2

        ndp[0] = max(ndp[0], dp[0] + ai)
        ndp[0] = max(ndp[0], dp[1])
        ndp[1] = max(ndp[1], dp[0])

        dp = ndp

    ans = dp[0]
    print(ans)


if __name__ == "__main__":
    main()
