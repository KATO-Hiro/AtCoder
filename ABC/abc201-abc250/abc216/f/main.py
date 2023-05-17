# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ab = list()

    for ai, bi in zip(a, b):
        ab.append((ai, bi))

    ab = sorted(ab)

    n_max = 5000
    dp = [1] * (n_max + 1)
    mod = 998244353
    ans = 0

    for i in range(n):
        ai, bi = ab[i]

        if ai >= bi:
            ans += dp[ai - bi]
            ans %= mod

        for j in range(n_max - bi, -1, -1):
            dp[j + bi] += dp[j]
            dp[j + bi] %= mod

    print(ans)


if __name__ == "__main__":
    main()
