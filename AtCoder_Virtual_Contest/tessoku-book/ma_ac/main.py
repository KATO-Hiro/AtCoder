# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    dp = [0, 0]

    for ai in a:
        ndp = [0, 0]

        ndp[0] = max(ndp[0], dp[0])
        ndp[1] = max(ndp[1], dp[0] + ai)
        ndp[0] = max(ndp[0], dp[1])

        dp = ndp

    print(max(dp))


if __name__ == "__main__":
    main()
