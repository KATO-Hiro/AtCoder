# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    size = 105
    pending = -1
    dp = [[pending for _ in range(size)] for _ in range(size)]
    dp[0][0] = 0

    for i, ai in enumerate(a):
        ndp = [[pending for _ in range(size)] for _ in range(size)]

        for j in range(i + 1):
            for x in range(d):
                if dp[j][x] == pending:
                    continue

                ndp[j][x] = max(ndp[j][x], dp[j][x])

                nj, nx = j + 1, (x + ai) % d
                ndp[nj][nx] = max(ndp[nj][nx], dp[j][x] + ai)

        dp = ndp

    print(dp[k][0])


if __name__ == "__main__":
    main()
