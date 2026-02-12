# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    size = 2 * m + 1
    pending = -1
    dp = [pending] * size
    dp[m] = 0

    for i in range(n):
        ai, bi = map(int, input().split())
        ndp = [pending] * size

        for j in range(size):
            if dp[j] == pending:
                continue

            nj = j + ai

            if nj < size:
                ndp[nj] = max(ndp[nj], dp[j] + ai)

            nj = j - bi

            if nj >= 0:
                ndp[nj] = max(ndp[nj], dp[j])

        dp = ndp

    print(max(dp))


if __name__ == "__main__":
    main()
