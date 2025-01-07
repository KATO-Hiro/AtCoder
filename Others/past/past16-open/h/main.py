# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    inf = 10**18
    dp = [[-inf for _ in range(2)] for _ in range(m + 1)]
    dp[0][0] = 0

    for ai in a:
        ndp = [[-inf for _ in range(2)] for _ in range(m + 1)]

        for j in range(m + 1):
            # 遊ぶ -> 遊ぶ
            # 宿題 -> 遊ぶ
            ndp[j][0] = max(dp[j]) + ai

            # 遊ぶ -> 宿題
            if j >= 1:
                ndp[j][1] = max(ndp[j][1], dp[j - 1][0])

        dp = ndp

    print(max(dp[m]))


if __name__ == "__main__":
    main()
