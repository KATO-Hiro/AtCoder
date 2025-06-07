# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    inf = 10**18
    dp = [-inf] * 100
    dp[0] = 0

    # dp[i][j]: i番目まで商品を選んだときに、購入金額 % 100 が j となるときのスコアの最大値
    for _ in range(n):
        pi, ui = map(int, input().split())
        ndp = [-inf] * 100

        for j in range(100):
            # 商品iを選ばない
            ndp[j] = max(ndp[j], dp[j])

            # 商品iを選ぶ
            nj = (j + pi) % 100
            ndp[nj] = max(ndp[nj], dp[j] + ui - pi + (j + pi) // 100 * 20)

        dp = ndp

    print(max(dp))


if __name__ == "__main__":
    main()
