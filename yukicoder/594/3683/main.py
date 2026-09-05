# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    inf = 10**18
    dp = [[-inf for _ in range(2)] for _ in range(k + 1)]
    dp[0][0] = 0

    for i, ai in enumerate(a):
        ndp = [[-inf for _ in range(2)] for _ in range(k + 1)]

        for j in range(k + 1):
            ndp[j][0] = max(ndp[j][0], dp[j][0], dp[j][1])

            nj = j + 1

            if nj > k:
                continue

            ndp[nj][1] = max(ndp[nj][1], dp[j][0] + ai)

        dp = ndp

    ans = max(dp[k])

    if ans < -(10**15):
        ans = "Impossible"

    print(ans)


if __name__ == "__main__":
    main()
