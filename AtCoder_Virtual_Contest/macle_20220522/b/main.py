# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input().rstrip()
    hands = [-1] * n
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        ti = t[i - 1]

        # あいこ or 負け
        dp[i] = dp[i - 1]

        # 勝ち
        score = 0

        if ti == "r":
            hand, score = 2, p
        elif ti == "s":
            hand, score = 0, r
        else:
            hand, score = 1, s

        # k回前の手と同じ場合は選ぶことができない
        if (i - k >= 0) and (hands[i - k - 1] == hand):
            continue

        dp[i] = dp[i - 1] + score
        hands[i - 1] = hand
    
    print(dp[n])


if __name__ == "__main__":
    main()
