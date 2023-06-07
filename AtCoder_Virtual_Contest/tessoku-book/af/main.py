# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, a, b = map(int, input().split())
    dp = [[False for _ in range(2)] for _ in range(n + 1)]
    dp[n][0] = True

    for i in range(n, -1, -1):
        if dp[i][0]:
            if i - a >= 0:
                dp[i - a][1] = True
            if i - b >= 0:
                dp[i - b][1] = True

        if dp[i][1]:
            if i - a >= 0:
                dp[i - a][0] = True
            if i - b >= 0:
                dp[i - b][0] = True

    print(dp)
    print(dp[0])


if __name__ == "__main__":
    main()
