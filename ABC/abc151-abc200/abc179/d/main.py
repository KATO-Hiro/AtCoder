# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    mod = 998244353
    left = [0 for _ in range(k)]
    right = [0 for _ in range(k)]
    dp = [0 for _ in range(n + 10)]
    dp[1] = 1
    imos = [0 for _ in range(n + 10)]

    for i in range(k):
        li, ri = map(int, input().split())

        left[i] = li
        right[i] = ri

    for i in range(1, n + 1):
        dp[i] += imos[i]
        dp[i] %= mod

        for l, r in zip(left, right):
            next_left = i + l
            next_right = i + r + 1

            if next_left > n:
                continue
            imos[next_left] += dp[i]
            imos[next_left] %= mod

            if next_right > n:
                continue
            imos[next_right] -= dp[i]
            imos[next_right] %= mod

        imos[i + 1] += imos[i]
        imos[i + 1] %= mod

    print(dp[n])


if __name__ == "__main__":
    main()
