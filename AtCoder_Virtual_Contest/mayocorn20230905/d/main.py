# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    n = len(s)
    size = 3010
    # size = 30
    pending = -1
    dp = [pending] * size
    dp[0] = 1
    mod = 998244353

    for i, si in enumerate(s):
        ndp = [0] * size

        for j in range(size):
            if dp[j] == pending:
                continue

            if si == "(" and (j + 1) < size:
                ndp[j + 1] += dp[j]
                ndp[j + 1] %= mod
            elif si == ")" and j >= 1:
                ndp[j - 1] += dp[j]
                ndp[j - 1] %= mod
            elif si == "?":
                if (j + 1) < size:
                    ndp[j + 1] += dp[j]
                    ndp[j + 1] %= mod
                if j >= 1:
                    ndp[j - 1] += dp[j]
                    ndp[j - 1] %= mod

        dp = ndp
        # print(dp)

    print(dp[0])


if __name__ == "__main__":
    main()
