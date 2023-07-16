# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    # dp[i][j]: i番目までの要素を使って、累積和がj(0 or 1)になる場合の数
    dp = [0] * 2
    ans = 0

    for si in s:
        ndp = [0] * 2
        ndp[int(si)] += 1

        if si == "0":
            ndp[1] += dp[0]
            ndp[1] += dp[1]
        else:
            ndp[1] += dp[0]
            ndp[0] += dp[1]

        dp = ndp
        ans += dp[1]

    print(ans)


if __name__ == "__main__":
    main()
