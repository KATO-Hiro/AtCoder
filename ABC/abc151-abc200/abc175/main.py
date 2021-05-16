# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    r, c, n = map(int, input().split())
    values = [[0 for _ in range(r + 1)] for __ in range(c + 1)]
    dp = [[0 for ___ in range(4)] for __ in range(r + 5)]

    for _ in range(n):
        ri, ci, vi = map(int, input().split())
        values[ci][ri] = vi

    for cj in range(1, c + 1):
        value = values[cj]

        for ri in range(1, r + 1):
            dpr = dp[ri]
            dpr[0] = max(dpr[0], max(dp[ri - 1]))
            v = value[ri]

            if v:
                for i in range(3, 0, -1):
                    dpr[i] = max(dpr[i], dpr[i - 1] + v)

    print(max(dp[r]))


if __name__ == "__main__":
    main()
