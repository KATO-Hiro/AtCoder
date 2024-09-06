# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    # [逃す / 倒す][倒した数 % 2]
    inf = 10**18
    dp = [[-inf for _ in range(2)] for _ in range(2)]
    dp[0][0] = 0

    for ai in a:
        ndp = [[-inf for _ in range(2)] for _ in range(2)]

        # 逃す
        ndp[0][0] = max(ndp[0][0], dp[0][0], dp[1][0])
        ndp[0][1] = max(ndp[0][1], dp[0][1], dp[1][1])

        # 倒す
        ndp[1][1] = max(ndp[1][1], max(dp[0][0], dp[1][0]) + ai)
        ndp[1][0] = max(ndp[1][0], max(dp[0][1], dp[1][1]) + 2 * ai)

        dp = ndp

    ans = 0

    for dp_i in dp:
        ans = max(ans, max(dp_i))

    print(ans)


if __name__ == "__main__":
    main()
