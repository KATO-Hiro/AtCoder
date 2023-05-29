# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    dp = [True] * 2

    for i in range(n - 1):
        ndp = [False] * 2

        if dp[0]:
            if abs(a[i] - a[i + 1]) <= k:
                ndp[0] = True
            if abs(a[i] - b[i + 1]) <= k:
                ndp[1] = True

        if dp[1]:
            if abs(b[i] - a[i + 1]) <= k:
                ndp[0] = True
            if abs(b[i] - b[i + 1]) <= k:
                ndp[1] = True

        dp = ndp

    if True in dp:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
