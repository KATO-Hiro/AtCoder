# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, a, b, p, q = map(int, input().split())
    # dp[i][j][flag]: 先手が地点i、後手が地点jにいるときに次の手番が先手/後手のときの先手の勝率
    dp = [[[0, 0] for _ in range(n + 1)] for _ in range(n + 1)]
    mod = 998244353
    inv_p = pow(p, mod - 2, mod)  # 1 / p 
    inv_q = pow(q, mod - 2, mod)  # 1 / q

    for i in range(n, a - 1, -1):
        for j in range(n, b - 1, -1):
            if i == n:
                dp[i][j] = [1, 1] # 先手が確実に勝つ
                pass
            elif j == n:
                dp[i][j] = [0, 0] # 先手が確実に負ける
            else:
                for pi in range(1, p + 1):
                    dp[i][j][0] += dp[min(i + pi, n)][j][1]

                dp[i][j][0] *= inv_p
                dp[i][j][0] %= mod

                for qj in range(1, q + 1):
                    dp[i][j][1] += dp[i][min(j + qj, n)][0]

                dp[i][j][1] *= inv_q
                dp[i][j][1] %= mod
    
    print(dp[a][b][0])


if __name__ == "__main__":
    main()
