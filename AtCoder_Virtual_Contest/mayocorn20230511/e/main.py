# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = [0] + list(map(int, input().split()))

    # Greedyを適用しにくいので、全探索 + 高速化 = DP
    # 円環だと扱いづらい + 曜日は対称性がある => ある日を休日と決め打ち
    # 休日間の部分しか影響しない = 直線状に切りひらいて、両端が休日 + その間をどうするかと言い換え
    # 前計算: 連続した平日がw日の場合の生産量
    b = [0] * (n + 1)

    for w in range(n + 1):
        for x in range(1, w):
            y = w - x
            b[w] += a[min(x, y)]

    # 最後の休日がi日目のときの生産量の最大値
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i):
            dp[i] = max(dp[i], dp[j] + b[i - j])

    print(dp[n])


if __name__ == "__main__":
    main()
