# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = [int(input()) for _ in range(n)]
    size_max = n
    dp = [1] * size_max

    for i, ai in enumerate(a):
        for j in range(i):
            if ai > a[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))


if __name__ == "__main__":
    main()
