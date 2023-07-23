# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = [0] * m
    b = [0] * m
    c = [0] * m

    for i in range(m):
        ai, bi = map(int, input().split())
        a[i], b[i] = ai, bi
        ci = list(map(int, input().split()))
        bit = 0

        for cij in ci:
            bit |= 1 << (cij - 1)

        c[i] = bit

    inf = 10**18
    dp = [inf] * (1 << (n + 3))
    dp[0] = 0

    for ai, ci in zip(a, c):
        ndp = [inf] * (1 << (n + 3))

        for bit in range(1 << n):
            ndp[bit] = min(ndp[bit], dp[bit])
            ndp[bit | ci] = min(ndp[bit | ci], dp[bit] + ai)

        dp = ndp

    ans = dp[(1 << n) - 1]

    if ans == inf:
        ans = -1

    print(ans)


if __name__ == "__main__":
    main()
