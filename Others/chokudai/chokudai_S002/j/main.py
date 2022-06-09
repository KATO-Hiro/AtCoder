# -*- coding: utf-8 -*-


def main():
    from math import gcd
    import sys

    input = sys.stdin.readline

    n = int(input())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    dp = [ab[0][0], ab[0][1]]

    for i in range(1, n):
        ndp = [0] * 2
        ai, bi = ab[i]

        for j in range(2):
            ndp[j] = max(ndp[j], gcd(dp[j], ai))
            ndp[j] = max(ndp[j], gcd(dp[j], bi))

        dp = ndp
    
    print(max(dp))


if __name__ == "__main__":
    main()
