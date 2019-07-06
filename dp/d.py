# -*- coding: utf-8 -*-


def main():
    n, w = map(int, input().split())
    ws = [0 for _ in range(n)]
    vs = [0 for _ in range(n)]
    dp = [[0 for _ in range(w + 1)] for _ in range(n + 1)]

    for i in range(n):
        wi, vi = map(int, input().split())
        ws[i] = wi
        vs[i] = vi

    for i in range(n):
        for sum_w in range(w + 1):
            if sum_w - ws[i] >= 0:
                dp[i + 1][sum_w] = max(dp[i + 1][sum_w],
                                       dp[i][sum_w - ws[i]] + vs[i])

            dp[i + 1][sum_w] = max(dp[i + 1][sum_w], dp[i][sum_w])

    print(dp[n][w])


if __name__ == '__main__':
    main()
