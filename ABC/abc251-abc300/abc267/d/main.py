# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    value_max = 2010
    inf = 10 ** 12
    dp = [-inf] * value_max
    dp[0] = 0

    for j in range(n):
        ndp = [-inf] * value_max

        for i in range(m + 1):
            if dp[i] == -1:
                continue

            ndp[i] = max(ndp[i], dp[i])
            ndp[i + 1] = max(ndp[i + 1], dp[i] + (i + 1) * a[j])

        dp = ndp

    print(dp[m])


if __name__ == "__main__":
    main()
