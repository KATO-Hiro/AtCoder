# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = list(map(int, input().split()))
    ss = [0] + s + s
    t = list(map(int, input().split()))
    tt = t + t
    inf = 10 ** 20
    dp = [inf for _ in range(2 * n + 10)]
    dp[0] = tt[0]

    for i in range(2 * n - 1):
        dp[i + 1] = min(dp[i + 1], dp[i] + ss[i + 1], tt[i + 1])

    for i in range(n):
        if dp[i + n] < dp[i]:
            dp[i] = dp[i + n]

    for i in range(n):
        print(dp[i])


if __name__ == "__main__":
    main()
