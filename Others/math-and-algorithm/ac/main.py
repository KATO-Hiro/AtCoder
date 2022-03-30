# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    dp = [0] * (n + 10)
    dp[1] = a[0]

    for i in range(2, n + 1):
        dp[i] = max(dp[i], dp[i - 1], dp[i - 2] + a[i - 1])
    
    print(dp[n])


if __name__ == "__main__":
    main()
