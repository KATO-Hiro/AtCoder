# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = list(reversed(list(input().rstrip()))) + ["0"]
    n = len(s)
    inf = 10 ** 20
    dp = [[inf for _ in range(2)] for _ in range(n + 10)]
    dp[0][0] = 0

    for i in range(n):
        for j in range(2):
            c = int(s[i])
            c += j

            if c < 10:
                dp[i + 1][0] = min(dp[i + 1][0], dp[i][j] + c)
            if c > 0:
                dp[i + 1][1] = min(dp[i + 1][1], dp[i][j] + (10 - c))
    
    print(min(dp[n][0], dp[n][1] + 1))


if __name__ == "__main__":
    main()
