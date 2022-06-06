# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    inf = float('inf')
    dp = [inf] * (n // 1000 + 10)
    dp[0] = 0

    for i in range(1, n // 1000 + 1):
        for j in [1, 5, 10]:
            if (i - j) < 0:
                continue

            dp[i] = min(dp[i], dp[i - j] + 1)
    
    print(dp[n // 1000])


if __name__ == "__main__":
    main()
