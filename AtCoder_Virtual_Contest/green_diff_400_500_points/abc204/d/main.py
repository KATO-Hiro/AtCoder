# -*- coding: utf-8 -*-


def main():
    import sys
    from math import ceil

    input = sys.stdin.readline

    n = int(input())
    t = list(map(int, input().split()))

    # 片方のオーブンを使うかどうかを決めたときの調理時間 = 部分和問題
    # Σt / 2以上となる最小値
    t_max = 10**5
    dp = [False] * (t_max + 1)
    dp[0] = True

    for i in range(n):
        ti = t[i]
        ndp = [False] * (t_max + 1)

        for j in range(t_max + 1):
            if not dp[j]:
                continue

            ndp[j] = True

            if j + ti > t_max:
                continue

            ndp[j + ti] = True

        dp = ndp

    t_half = ceil(sum(t) / 2)

    for i, dp_i in enumerate(dp):
        if i >= t_half and dp_i:
            print(i)
            exit()


if __name__ == "__main__":
    main()
