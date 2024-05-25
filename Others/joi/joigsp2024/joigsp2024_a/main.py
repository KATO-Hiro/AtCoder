# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    x = sorted(list(map(int, input().split())))

    if n == 2:
        print(x[1] - x[0])
        exit()

    inf = 10**18
    dp = [inf] * (n + 10)
    dp[1] = x[1] - x[0]
    dp[2] = x[2] - x[0]

    for i in range(3, n):
        dp[i] = min(dp[i], dp[i - 2] + x[i] - x[i - 1], dp[i - 3] + x[i] - x[i - 2])

    ans = dp[n - 1]
    print(ans)


if __name__ == "__main__":
    main()
