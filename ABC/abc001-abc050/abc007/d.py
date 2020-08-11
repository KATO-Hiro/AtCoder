# -*- coding: utf-8 -*-


def count_banned_numbers(s):
    n = len(s)
    # dp[digit][smaller][include 4 or 9]
    dp = [[[0 for _ in range(2)] for _ in range(2)] for _ in range(n + 10)]
    dp[0][0][0] = 1

    for i in range(n):
        for j in range(2):
            for k in range(2):
                nd = int(s[i])

                for digit in range(10):
                    ni, nj, nk = i + 1, j, k

                    if digit == 4 or digit == 9:
                        nj = 1

                    if k == 0:
                        if digit > nd:
                            continue
                        elif digit < nd:
                            nk = 1

                    dp[ni][nj][nk] += dp[i][j][k]

    return dp[n][1][0] + dp[n][1][1]


def main():
    a, b = input().split()
    a = str(int(a) - 1)
    print(count_banned_numbers(b) - count_banned_numbers(a))


if __name__ == '__main__':
    main()
