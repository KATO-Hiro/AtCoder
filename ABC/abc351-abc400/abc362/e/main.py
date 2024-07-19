# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    size = 81
    # 最後にi番目、j = i - 1番目を選び、部分列の長さがk個のときに条件を満たす個数
    dp = [[[0 for _ in range(size)] for _ in range(size)] for _ in range(size)]
    mod = 998244353

    # 初期化: n >= 2のときを考える
    for i in range(n):
        for j in range(i):
            dp[i][j][2] += 1

    for i in range(n):
        for j in range(i):
            for k in range(2, n):
                now = dp[i][j][k]

                if now == 0:
                    continue

                for x in range(i + 1, n):
                    # 等差か判定
                    if a[x] - a[i] != a[i] - a[j]:
                        continue

                    dp[x][i][k + 1] += now
                    dp[x][i][k + 1] %= mod

    ans = [0] * size
    ans[1] = n  # 長さ1のときは必ず条件を満たす

    for k in range(2, size):
        for i in range(size):
            for j in range(i):
                ans[k] += dp[i][j][k]
                ans[k] %= mod

    print(*ans[1 : n + 1])


if __name__ == "__main__":
    main()
