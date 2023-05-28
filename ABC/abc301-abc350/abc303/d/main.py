# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x, y, z = map(int, input().split())
    s = input().rstrip()
    inf = 10**18
    dp = [inf] * 2
    dp[0] = 0

    for si in s:
        ndp = [inf] * 2

        if si == "a":
            ndp[0] = min(ndp[0], dp[0] + x)
            ndp[1] = min(ndp[1], dp[0] + z + y)
            ndp[0] = min(ndp[0], dp[1] + z + x)
            ndp[1] = min(ndp[1], dp[1] + y)
        else:
            ndp[0] = min(ndp[0], dp[0] + y)
            ndp[1] = min(ndp[1], dp[0] + z + x)
            ndp[0] = min(ndp[0], dp[1] + z + y)
            ndp[1] = min(ndp[1], dp[1] + x)

        dp = ndp

    print(min(dp))


if __name__ == "__main__":
    main()
