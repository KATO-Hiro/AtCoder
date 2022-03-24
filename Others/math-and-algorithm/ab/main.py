# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    dp = [0] * (n + 10)
    dp[0] = 1

    for i in range(n):
        dp[i + 1] += dp[i]
        dp[i + 2] += dp[i]
    
    print(dp[n])



if __name__ == "__main__":
    main()
