# -*- coding: utf-8 -*-


def main():
    n = int(input())
    abc = [[0 for _ in range(3)] for _ in range(n)]
    dp = [[0 for _ in range(3)] for _ in range(n + 1)]

    for i in range(n):
        ai, bi, ci = map(int, input().split())
        abc[i][0] = ai
        abc[i][1] = bi
        abc[i][2] = ci

    # See:
    # https://qiita.com/drken/items/dc53c683d6de8aeacf5a
    for i in range(n):
        for j in range(3):
            for k in range(3):
                if j == k:
                    continue

                dp[i + 1][k] = max(dp[i + 1][k], dp[i][j] + abc[i][k])

    print(max(dp[n]))


if __name__ == '__main__':
    main()
