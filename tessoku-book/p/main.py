# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = [0] * 2 + list(map(int, input().split()))
    b = [0] * 3 + list(map(int, input().split()))
    inf = 10 ** 9
    dp = [inf] * (n + 1)
    dp[0] = dp[1] = 0

    for i in range(2, n + 1):
        dp[i] = min(dp[i], dp[i - 1] + a[i])

        if i >= 3:
            dp[i] = min(dp[i], dp[i - 2] + b[i])

    print(dp[n])
    

if __name__ == "__main__":
    main()
