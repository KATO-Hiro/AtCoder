# -*- coding: utf-8 -*-


def main():
    n, w = map(int, input().split())
    ws = [0 for _ in range(n)]
    vs = [0 for _ in range(n)]
    inf = 10 ** 12
    dp = [[inf for _ in range(((n + 1) * 10 ** 3) + 1)] for _ in range(n + 1)]

    for i in range(n):
        wi, vi = map(int, input().split())
        ws[i] = wi
        vs[i] = vi

    dp[0][0] = 0

    for i in range(n):
        for sum_v in range(((n + 1) * 10 ** 3) + 1):
            if sum_v - vs[i] >= 0:
                dp[i + 1][sum_v] = min(dp[i + 1][sum_v],
                                       dp[i][sum_v - vs[i]] + ws[i])

            dp[i + 1][sum_v] = min(dp[i + 1][sum_v], dp[i][sum_v])

    ans = 0

    for index, d in enumerate(dp[n]):
        if d <= w:
            ans = index

    print(ans)


if __name__ == '__main__':
    main()
