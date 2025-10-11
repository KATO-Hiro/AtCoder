# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))

    dp = [0, a[0]]
    count = [0, 1]
    mod = 10**9 + 7

    for ai in a[1:]:
        ndp = [0, 0]
        ncount = [0, 0]

        ndp[0] = dp[1] - ai * count[1]
        ndp[0] %= mod
        ndp[1] = sum(dp) + ai * sum(count)
        ndp[1] %= mod

        ncount[0] = count[1]
        ncount[0] %= mod
        ncount[1] = sum(count)
        ncount[1] %= mod

        dp = ndp
        count = ncount

    print(sum(dp) % mod)


if __name__ == "__main__":
    main()
