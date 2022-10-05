# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        for ai in a:
            if i < ai:
                continue

            dp[i] = max(dp[i], ai + (i - ai) - dp[i - ai])
    
    print(dp[n])


if __name__ == "__main__":
    main()
