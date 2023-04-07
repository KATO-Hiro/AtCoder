# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    inf = 10 ** 18
    dp = [-inf] * (m + 1)
    dp[0] = 0

    for i in range(n):
        ndp = [-inf] * (m + 1)

        for j in range(m + 1):
            if dp[j] == -inf:
                continue

            ndp[j] = max(ndp[j], dp[j])

            if j + 1 <= m:
                ndp[j + 1] = max(ndp[j + 1], dp[j] + (j + 1) * a[i])

        dp = ndp
    
    print(dp[m])


if __name__ == "__main__":
    main()
