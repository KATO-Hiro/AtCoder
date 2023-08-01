# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    inf = 10**18
    dp = [inf] * (1 << n)
    dp[0] = 0

    for _ in range(m):
        si, ci = map(str, input().split())
        si = int(si.replace("Y", "1").replace("N", "0"), 2)
        ci = int(ci)
        ndp = [inf] * (1 << n)

        for j in range(1 << n):
            if dp[j] == inf:
                continue

            ndp[j] = min(ndp[j], dp[j])
            ndp[j | si] = min(ndp[j | si], dp[j] + ci)

        dp = ndp

    ans = dp[(1 << n) - 1]

    if ans == inf:
        ans = -1

    print(ans)


if __name__ == "__main__":
    main()
