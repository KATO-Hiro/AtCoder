# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x = map(int, input().split())
    inf = 10**18
    dp = [(-inf, -inf)] * (x + 1)
    dp[0] = (0, 10**9)  # 金貨、銀貨の枚数

    for i in range(n):
        ai, bi, ci = map(int, input().split())
        ndp = [(-inf, -inf)] * (x + 1)

        for j in range(x + 1):
            if dp[j] == (-inf, -inf):
                continue

            ndp[j] = max(ndp[j], dp[j])

            if j + bi > x:
                continue

            ndp[j + bi] = max(ndp[j + bi], (dp[j][0] + ci, dp[j][1] - ai))

        dp = ndp

    ans = (-inf, -inf, -inf)

    for ri, (pi, qi) in enumerate(dp):
        ans = max(ans, (pi, qi, x - ri))

    print(*ans)


if __name__ == "__main__":
    main()
