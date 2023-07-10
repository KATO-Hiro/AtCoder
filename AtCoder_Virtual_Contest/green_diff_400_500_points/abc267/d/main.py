# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    inf = 10**12
    dp = [-inf] * (m + 1)
    dp[0] = 0

    for i in range(n):
        ai = a[i]

        for j in range(m, 0, -1):
            dp[j] = max(dp[j], dp[j - 1] + j * ai)

    print(dp[m])


if __name__ == "__main__":
    main()
