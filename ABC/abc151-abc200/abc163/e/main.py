# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    p = list()

    for i, ai in enumerate(a):
        p.append((ai, i))
    
    p = sorted(p, reverse=True)

    size = 2010
    dp = [[0] * size for _ in range(size)]

    for i in range(n):
        _, pi = p[i]

        for left in range(i + 1):
            right = i - left

            dp[i + 1][left + 1] = max(dp[i + 1][left + 1], dp[i][left] + a[pi] * (pi - left))
            dp[i + 1][left] = max(dp[i + 1][left], dp[i][left] + a[pi] * ((n - right - 1) - pi))
        
    print(max(dp[n]))


if __name__ == "__main__":
    main()
