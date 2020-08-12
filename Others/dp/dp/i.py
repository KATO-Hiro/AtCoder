# -*- coding: utf-8 -*-


def main():
    n = int(input())
    p = list(map(float, input().split()))
    dp = [[0 for _ in range(n + 100)] for _ in range(n + 100)]

    # 初期化
    dp[0][0] = 1.0

    # KeyInsight
    # dp[i][j] := 最初の i 枚のコインを投げたときに、表が j 枚となる確率
    # ・状態：確率
    # ・すべての候補，条件に一致する候補をdpで管理
    # See:
    # https://qiita.com/drken/items/03c7db44ccd27820ea0d#i-%E5%95%8F%E9%A1%8C---coins
    for i in range(n):
        for j in range(i + 1):
            # 表
            dp[i + 1][j + 1] += dp[i][j] * p[i]
            # 裏
            dp[i + 1][j] += dp[i][j] * (1 - p[i])

    ans = 0

    # 表が多い場合のみ計算
    for j in range((n + 1) // 2, n + 1):
        ans += dp[n][j]

    print(ans)


if __name__ == '__main__':
    main()
