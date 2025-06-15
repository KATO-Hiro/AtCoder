# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, h, m = map(int, input().split())
    inf = 10**18
    dp = [[-inf for _ in range(h + 1)] for _ in range(n + 1)]
    dp[0][h] = m

    for i in range(n):
        ai, bi = map(int, input().split())

        for j in range(h + 1):
            if dp[i][j] == -inf:
                continue

            nj = j - ai

            if nj >= 0:
                dp[i + 1][nj] = max(dp[i + 1][nj], dp[i][j])

            if dp[i][j] >= bi:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] - bi)

        if set(dp[i + 1]) == set([-inf]):
            print(i)
            exit()

    print(n)


if __name__ == "__main__":
    main()
