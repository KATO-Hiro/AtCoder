# -*- coding: utf-8 -*-


def main():
    import sys
    from math import ceil

    input = sys.stdin.readline

    n = int(input())
    t = list(map(int, input().split()))

    # 1つのオーブンで料理を選ぶ・選ばない = 部分和問題
    # n種類の料理を選び終えたとき、総所要時間の半分より大きい & True
    time_max = 10**5 + 1
    dp = [False] * time_max
    dp[0] = True

    for i, ti in enumerate(t):
        ndp = [False] * time_max

        for j in range(time_max):
            if not dp[j]:
                continue

            ndp[j] = True
            nj = j + ti

            if nj < time_max:
                ndp[nj] = True

        dp = ndp

    time_total = sum(t)
    time_half = ceil(time_total / 2)

    for i, dp_i in enumerate(dp):
        if i >= time_half and dp_i:
            print(i)
            exit()


if __name__ == "__main__":
    main()
