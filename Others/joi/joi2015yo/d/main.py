# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    d = [int(input()) for _ in range(n)]
    c = [int(input()) for _ in range(m)]
    inf = 10**18
    dp = [inf] * (n + 1)
    dp[0] = 0
    ans = inf

    # print(d)
    # print(c)

    for j, cj in enumerate(c):
        ndp = [inf] * (n + 1)

        for i in range(n + 1):
            ndp[i] = min(ndp[i], dp[i])

            if i - 1 >= 0:
                di = d[i - 1]
                ndp[i] = min(ndp[i], dp[i - 1] + di * cj)

        dp = ndp

        if j >= n:
            ans = min(ans, dp[n])

    print(ans)


if __name__ == "__main__":
    main()
