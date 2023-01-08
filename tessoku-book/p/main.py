# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = [0] * 1 + list(map(int, input().split()))
    b = [0] * 2 + list(map(int, input().split()))
    inf = 10 ** 9
    dp = [inf] * n
    dp[0], dp[1] = 0, a[1]

    for i in range(2, n):
        dp[i] = min(dp[i - 1] + a[i], dp[i - 2] + b[i])

    print(dp[n - 1])
    

if __name__ == "__main__":
    main()
