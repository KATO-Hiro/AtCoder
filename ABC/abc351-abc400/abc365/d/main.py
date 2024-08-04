# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    dp = [0] * 3  # R, S, P

    # 引き分け以上を選び続ける
    for si in s:
        ndp = [0] * 3

        if si == "R":
            ndp[2] = max(ndp[2], max(dp[0], dp[1]) + 1)
            ndp[0] = max(ndp[0], dp[1], dp[2])
        elif si == "S":
            ndp[0] = max(ndp[0], max(dp[1], dp[2]) + 1)
            ndp[1] = max(ndp[1], dp[0], dp[2])
        else:
            ndp[1] = max(ndp[1], max(dp[0], dp[2]) + 1)
            ndp[2] = max(ndp[2], dp[0], dp[1])

        dp = ndp

    print(max(dp))


if __name__ == "__main__":
    main()
