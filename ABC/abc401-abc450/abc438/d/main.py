# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    b[0] = c[0] = c[1] = 0
    dp = [0] * 3
    dp[0] = a[0]

    for i in range(1, n):
        ndp = [0] * 3

        ndp[0] = max(ndp[0], dp[0] + a[i])
        ndp[1] = max(ndp[1], max(dp[0], dp[1]) + b[i])
        ndp[2] = max(ndp[2], max(dp[1], dp[2]) + c[i])

        dp = ndp

    ans = dp[2]
    print(ans)


if __name__ == "__main__":
    main()
