# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [False] * (n + 1)

    for i in range(n + 1):
        dp[i] = any(not dp[i - ai] for ai in a if i >= ai)

    if dp[n]:
        print("First")
    else:
        print("Second")


if __name__ == "__main__":
    main()
