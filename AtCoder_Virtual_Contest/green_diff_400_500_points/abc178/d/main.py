# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = int(input())

    # 総和Sを玉が並んでいる状態と言い換え
    # 各項が1の場合なら、2 ** (S - 1)通りだが、全てが3項以上と指定がある
    # i番目の玉の状態になるには、[0, i - 3]までの状態が必要
    dp = [0] * (s + 1)
    dp[0] = 1
    mod = 10**9 + 7

    for i in range(1, s + 1):
        for j in range(i - 3 + 1):
            dp[i] += dp[j]
            dp[i] %= mod

    print(dp[s])


if __name__ == "__main__":
    main()
