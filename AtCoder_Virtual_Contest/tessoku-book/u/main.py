# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    p, a = [0] * (n + 10), [0] * (n + 10)
    for i in range(1, n + 1):
        pi, ai = map(int, input().split())
        p[i] = pi
        a[i] = ai

    # 操作によりブロックを取り除くと、連続した要素が残る
    # dp[left][right]: 左側のブロックの位置left、右側のブロックの位置rightとしたときに、操作後に得られる得点の最大値。
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for size in range(n - 2, -1, -1):
        for left in range(1, n - size + 1):
            right = left + size
            score1, score2 = 0, 0

            if left <= p[left - 1] <= right:
                score1 = a[left - 1]
            if left <= p[right + 1] <= right:
                score2 = a[right + 1]

            if left == 1:
                dp[left][right] = max(dp[left][right], dp[left][right + 1] + score2)
            elif right == n:
                dp[left][right] = max(dp[left][right], dp[left - 1][right] + score1)
            else:
                dp[left][right] = max(
                    dp[left - 1][right] + score1, dp[left][right + 1] + score2
                )

    # dp[i][i] (i = 1, 2, ..., n)の最大値が答え
    ans = 0

    for i in range(1, n + 1):
        ans = max(ans, dp[i][i])

    print(ans)


if __name__ == "__main__":
    main()
