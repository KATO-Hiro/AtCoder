# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, ma, mb = map(int, input().split())
    inf = 10**18
    size = 410  # 薬品の最大の重量 + α
    dp = [[inf for _ in range(size)] for _ in range(size)]
    dp[0][0] = 0

    for i in range(n):
        ai, bi, ci = map(int, input().split())
        ndp = [[inf for _ in range(size)] for _ in range(size)]

        for j in range(size):
            for k in range(size):
                if dp[j][k] == inf:
                    continue

                ndp[j][k] = min(ndp[j][k], dp[j][k])

                nj, nk = j + ai, k + bi
                ndp[nj][nk] = min(ndp[nj][nk], dp[j][k] + ci)

        dp = ndp

    ans = inf

    for ratio in range(1, n + 1):
        new_ma = ratio * ma
        new_mb = ratio * mb

        ans = min(ans, dp[new_ma][new_mb])

    if ans == inf:
        ans = -1

    print(ans)


if __name__ == "__main__":
    main()
