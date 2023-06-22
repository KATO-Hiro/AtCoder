# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    dp = a[0]
    mod = 10**9 + 7

    for i in range(1, n):
        ndp = [1] * 6

        for j in range(6):
            ndp[j] *= dp[j] * sum(a[i])
            ndp[j] %= mod

        dp = ndp

    print(sum(dp) % mod)


if __name__ == "__main__":
    main()
