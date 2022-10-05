# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # dp[i][j]: 手番i、残りの個数jのときに、高橋君の石の数
    dp = [[0] * (n + 1) for _ in range(2)]

    # ゲームの問題は、最終局面から考える
    # akをいくつか選んで合計をnにする部分和問題 = DP

    for j in range(1, n + 1):
        # 高橋君
        candidate = 0

        for ai in a:
            if j - ai >= 0:
                candidate = max(candidate, dp[1][j - ai] + ai)
        
        dp[0][j] = candidate

        # 青木君
        candidate = float("inf")

        for ai in a:
            if j - ai >= 0:
                candidate = min(candidate, dp[0][j - ai])
        
        dp[1][j] = candidate

    print(dp[0][n])


if __name__ == "__main__":
    main()
