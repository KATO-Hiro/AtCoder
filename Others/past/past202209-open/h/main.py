# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x = map(int, input().split())
    inf = 10**18
    dp = [(-inf, -inf)] * (x + 1)
    dp[x] = (0, 10**9)  # 金貨、銀貨の枚数

    for _ in range(n):
        ai, bi, ci = map(int, input().split())

        for j in range(bi, x + 1):
            dp[j - bi] = max(dp[j - bi], (dp[j][0] + ci, dp[j][1] - ai))

    ans = (-inf, -inf, -inf)

    for ri, (pi, qi) in enumerate(dp):
        ans = max(ans, (pi, qi, ri))

    print(*ans)


if __name__ == "__main__":
    main()
