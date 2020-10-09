# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    s = int(input())
    mod = 10 ** 9 + 7
    dp = [0 for _ in range(s + 1)]
    dp[0] = 1

    # KeyInsight:
    # 数字を球が連続して並んでいる状態に言い換える
    # dp[i]: 最後に切った場所がi。両端も含める。
    for i in range(1, s + 1):
        for j in range(i - 3 + 1):
            dp[i] += dp[j]
            dp[i] %= mod

    print(dp[s])


if __name__ == '__main__':
    main()
