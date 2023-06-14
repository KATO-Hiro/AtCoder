# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, a, b = map(int, input().split())
    dp = [False] * (n + 1)

    for i in range(n + 1):
        if i >= a and not dp[i - a]:
            dp[i] = True
        elif i >= b and not dp[i - b]:
            dp[i] = True
        else:
            dp[i] = False

    if dp[n]:
        print("First")
    else:
        print("Second")


if __name__ == "__main__":
    main()
