# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    inf = 10**18
    dp = [-inf] * (m + 1)
    dp[0] = 0

    for _ in range(n):
        ti, pi = map(int, input().split())
        ndp = [-inf] * (m + 1)

        for j in range(m + 1):
            if dp[j] == -inf:
                continue

            ndp[j] = max(ndp[j], dp[j])

            nj = j + ti

            if nj > m:
                continue

            ndp[nj] = max(ndp[nj], dp[j] + pi)

        dp = ndp

    ans = max(dp)

    if ans == -inf:
        ans = 0

    print(ans)


if __name__ == "__main__":
    main()
