# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, a, b = map(int, input().split())
    wv = [tuple(map(int, input().split())) for _ in range(n)]
    dp = [[-1 for _ in range(b + 1)] for _ in range(a + 1)]
    dp[0][0] = 0

    # 可能な操作を列挙

    # 通常のナップサックDPに状態を一つ(= ナップサック2に入れる)追加
    # dp[i][j][k]: ナップサック1の重さj, 同2の重さkであるときのおいしさの最大値
    for i in range(n):
        wi, vi = wv[i]
        ndp = [[-1 for _ in range(b + 1)] for _ in range(a + 1)]

        # 貰うDP
        for j in range(a + 1):
            for k in range(b + 1):
                # i番目のお菓子をナップサックに入れない
                if dp[j][k] != -1:
                    ndp[j][k] = max(ndp[j][k], dp[j][k])

                # i番目のお菓子をナップサック1に入れる
                pj = j - wi

                if pj >= 0 and dp[pj][k] != -1:
                    ndp[j][k] = max(ndp[j][k], dp[pj][k] + vi)

                # i番目のお菓子をナップサック2に入れる
                pk = k - wi

                if pk >= 0 and dp[j][pk] != -1:
                    ndp[j][k] = max(ndp[j][k], dp[j][pk] + vi)

        dp = ndp

    ans = 0

    for j in range(a + 1):
        for k in range(b + 1):
            ans = max(ans, dp[j][k])

    print(ans)


if __name__ == "__main__":
    main()
