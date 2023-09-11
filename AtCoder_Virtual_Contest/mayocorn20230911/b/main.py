# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    s = s + s
    t = t + t
    inf = 10**20
    m = n * 2
    dp = [inf] * m
    dp[0] = t[0]

    for i in range(1, m):
        dp[i] = min(dp[i], t[i], dp[i - 1] + s[i - 1])

    ans = [inf] * n

    for i in range(n):
        ans[i] = min(dp[i], dp[i + n])

    # print(*dp, sep="\n")
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
