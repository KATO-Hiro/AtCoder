# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    size_max = 105
    inf = -1
    dp = [[inf for _ in range(size_max)] for _ in range(size_max)]
    dp[0][0] = 0

    for i, ai in enumerate(a):
        ndp = [[inf for _ in range(size_max)] for _ in range(size_max)]

        # i個以上選べない
        for j in range(i + 1):
            for x in range(d):
                if dp[j][x] == inf:
                    continue

                ndp[j][x] = max(ndp[j][x], dp[j][x])
                ndp[j + 1][(x + ai) % d] = max(ndp[j + 1][(x + ai) % d], dp[j][x] + ai)

        dp = ndp

    ans = dp[k][0]
    print(ans)


if __name__ == "__main__":
    main()
