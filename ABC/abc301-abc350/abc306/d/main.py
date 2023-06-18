# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    dp = [0, 0]

    for xi, yi in xy:
        ndp = [0, 0]

        if xi == 0:
            ndp[0] = max(ndp[0], dp[0] + yi)
            ndp[0] = max(ndp[0], dp[1] + yi)
        else:
            ndp[1] = max(ndp[1], dp[0] + yi)

        ndp[0] = max(ndp[0], dp[0])
        ndp[1] = max(ndp[1], dp[1])

        dp = ndp

    print(max(dp))


if __name__ == "__main__":
    main()
