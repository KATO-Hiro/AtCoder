# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    s = int(input())
    mod = 10 ** 9 + 7
    dp = [0 for _ in range(s + 1)]
    dp[0] = 1
    total = 0

    # KeyInsight:
    # 数字を球が連続して並んでいる状態に言い換える
    # dp[i]: 最後に切った場所がi。両端も含める。
    # 高速化: 累積和を保存する変数を用意 & 差分のみを更新

    # See:
    # https://www.youtube.com/watch?v=yLkJZXkB6D0&feature=youtu.be
    for i in range(1, s + 1):
        if (i - 3) >= 0:
            total += dp[i - 3]

        dp[i] += total
        dp[i] %= mod

    print(dp[s])


if __name__ == '__main__':
    main()
