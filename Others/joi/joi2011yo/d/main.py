# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    pending, size = -1, 21
    dp = [pending] * size
    dp[a[0]] = 1

    for i in range(1, n - 1):
        ai = a[i]
        ndp = [0] * size

        for j in range(size):
            if dp[j] == pending:
                continue

            nj1 = j - ai
            nj2 = j + ai

            if nj1 >= 0:
                ndp[nj1] += dp[j]
            if nj2 < size:
                ndp[nj2] += dp[j]

        dp = ndp

    print(dp[a[-1]])


if __name__ == "__main__":
    main()
