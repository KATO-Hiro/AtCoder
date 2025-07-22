# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    p = list(map(int, input().split()))

    ng, ok = -1, 10**18
    inf = 10**18

    def f(wj):
        dp = [[-inf for _ in range(w)] for _ in range(h)]
        dp[0][0] = wj

        for i in range(h):
            for j in range(w):
                dp[i][j] += a[i][j] - p[i + j]

                if dp[i][j] < 0:
                    dp[i][j] = -inf

                ni, nj = i + 1, j + 1

                if ni < h:
                    dp[ni][j] = max(dp[ni][j], dp[i][j])
                if nj < w:
                    dp[i][nj] = max(dp[i][nj], dp[i][j])

        return dp[h - 1][w - 1] >= 0

    while abs(ok - ng) > 1:
        wj = (ok + ng) // 2

        if f(wj):
            ok = wj
        else:
            ng = wj

    print(ok)


if __name__ == "__main__":
    main()
