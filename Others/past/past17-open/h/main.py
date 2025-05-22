# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    size = 5001
    ac = [[] for _ in range(size)]

    for _ in range(n):
        ai, bi, ci = map(int, input().split())
        bi -= 1

        # 時間biでまとめる
        ac[bi].append((ai, ci))

    inf = 10**18
    dp = [inf] * size
    dp[0] = 0

    for i in range(size - 1):
        ndp = [inf] * size

        for j in range(m + 1):
            if dp[j] == inf:
                continue

            ndp[j] = min(ndp[j], dp[j])

            for ai, ci in ac[i]:
                nj = min(m, j + ci)
                ndp[nj] = min(ndp[nj], dp[j] + ai)

        dp = ndp

    ans = dp[m]

    if ans == inf:
        ans = -1

    print(ans)


if __name__ == "__main__":
    main()
