# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    value_max = 2010
    inf = 10 ** 12
    dp = [-inf] * value_max
    dp[0] = 0

    for ai in a:
        for i in range(m, 0, -1):
            dp[i] = max(dp[i], dp[i - 1] + i * ai)

    print(dp[m])


if __name__ == "__main__":
    main()
