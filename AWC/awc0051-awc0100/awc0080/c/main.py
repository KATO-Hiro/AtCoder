# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    inf = 10**18
    dp = [-inf] * (k + 1)
    dp[0] = 0

    for _ in range(n):
        ti, ai = map(int, input().split())
        ndp = [-inf] * (k + 1)

        for j in range(k + 1):
            if dp[j] == -inf:
                continue

            ndp[j] = max(ndp[j], dp[j])

            if ti == 1:
                nj = j + 1

                if nj > k:
                    continue

                ndp[nj] = max(ndp[nj], dp[j] + ai)
            else:
                nj = max(0, j - 1)
                ndp[nj] = max(ndp[nj], dp[j] + ai)

        dp = ndp

    ans = max(0, dp[0])
    print(ans)


if __name__ == "__main__":
    main()
