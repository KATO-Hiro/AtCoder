# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict
    from itertools import accumulate

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = list(accumulate(a, initial=0))
    mod = 998244353
    dp = [0] * (n + 1)  # i番目まで決めたときの条件を満たす分割方法
    dp[0] = 1
    dp_total = 1
    dp_sum = defaultdict(int)
    dp_sum[0] = 1

    # 累積和と余事象を活用して高速化
    # dp[i]の和を変数で、dp_sum[si]を連想配列で持つ
    for i in range(1, n + 1):
        dp[i] += dp_total
        sj = s[i] - k
        dp[i] -= dp_sum[sj]
        dp[i] %= mod

        dp_total += dp[i]
        dp_total %= mod
        si = s[i]
        dp_sum[si] += dp[i]
        dp_sum[si] %= mod

    print(dp[n])


if __name__ == "__main__":
    main()
