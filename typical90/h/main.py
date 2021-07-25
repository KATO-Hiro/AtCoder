# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = input()
    t = list("atcoder")
    m = len(t)
    mod = 10 ** 9 + 7
    dp = [[0 for _ in range(m + 5)] for _ in range(n + 1)]
    dp[0][0] = 1

    for i, si in enumerate(s):
        for j in range(m + 1):
            dp[i + 1][j] += dp[i][j]

            if si in t and t.index(si) == j:
                dp[i + 1][j + 1] += dp[i][j]

        for j in range(m + 1):
            dp[i + 1][j] %= mod

    print(dp[n][m])


if __name__ == "__main__":
    main()
