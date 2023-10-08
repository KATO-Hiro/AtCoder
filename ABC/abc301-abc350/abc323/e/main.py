# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x = map(int, input().split())
    t = list(map(int, input().split()))
    mod = 998244353
    inv = pow(n, mod - 2, mod)  # 1 / p

    # ランダムに何曲か選ぶ + 最後に曲1を選んで、x秒より大きいときが答え
    # dp[i]: 再生がi秒で終わる確率
    dp = [0] * (x + 1)
    dp[0] = 1

    # 各時点において、すべての曲を試す
    for i in range(x + 1):
        for tj in t:
            ni = i + tj

            if ni > x:
                continue

            dp[ni] += dp[i] * inv
            dp[ni] %= mod

    ans = 0

    for i, dp_i in enumerate(dp):
        if i + t[0] > x:
            ans += dp_i * inv
            ans %= mod

    print(ans)


if __name__ == "__main__":
    main()
