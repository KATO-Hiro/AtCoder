# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    mod = 10 ** 9 + 7
    # dp[size][i][j][k]: 文字列の長さ、文字列の直前の1, 2, 3番目のとき、条件を満たす組み合わせ
    dp = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(n + 2)]
    dp[0][3][3][3] = 1 # 初期化

    for size in range(n + 1):
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    if dp[size][i][j][k] == 0:
                        continue

                    for new_s in range(4):
                        # 条件を満たさない場合を弾く
                        if new_s == 0 and i == 1 and j == 2:
                            continue
                        if new_s == 0 and i == 2 and j == 1:
                            continue
                        if new_s == 1 and i == 0 and j == 2:
                            continue
                        if new_s == 0 and i == 1 and k == 2:
                            continue
                        if new_s == 0 and j == 1 and k == 2:
                            continue

                        dp[size + 1][new_s][i][j] += dp[size][i][j][k]
                        dp[size + 1][new_s][i][j] %= mod
        
    ans = 0

    for i in range(4):
        for j in range(4):
            for k in range(4):
                ans += dp[n][i][j][k]
                ans %= mod
    
    print(ans)


if __name__ == "__main__":
    main()
