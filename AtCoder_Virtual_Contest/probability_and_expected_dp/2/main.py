# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    p = list(map(float, input().split()))
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(n):
        ndp = [0] * (n + 1)
        pi = p[i]

        for j in range(i + 1):
            # 裏
            ndp[j] += dp[j] * (1 - pi)

            # 表
            if j + 1 <= n:
                ndp[j + 1] += dp[j] * pi

        dp = ndp

    m = (n + 1) // 2
    # print(dp)
    print(sum(dp[m:]))


if __name__ == "__main__":
    main()
