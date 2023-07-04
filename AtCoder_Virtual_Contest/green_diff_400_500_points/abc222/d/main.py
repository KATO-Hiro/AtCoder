# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    size = 3010
    dp = [0] * size
    mod = 998244353

    # 初期化
    for i in range(a[0], b[0] + 1):
        dp[i] = 1

    for k in range(1, n):
        ak, bk = a[k], b[k]
        ndp = [0] * size

        for i in range(size):
            ak = max(i, ak)
            ndp[ak] += dp[i]
            ndp[bk + 1] -= dp[i]

        for j in range(size - 1):
            ndp[j + 1] += ndp[j]
            ndp[j] %= mod
            ndp[j + 1] %= mod

        dp = ndp

    print(sum(dp) % mod)


if __name__ == "__main__":
    main()
