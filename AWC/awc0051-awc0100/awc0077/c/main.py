# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    inf = 10**18
    dp = [inf] * (s + 1)
    dp[0] = 0

    for ai in a:
        ndp = [inf] * (s + 1)

        for j in range(s + 1):
            if dp[j] == inf:
                continue

            ndp[j] = min(ndp[j], dp[j])
            nj = j + ai

            if nj > s:
                continue

            ndp[nj] = min(ndp[nj], dp[j] + 1)

        dp = ndp

    ans = dp[-1]

    if ans == inf:
        ans = -1

    print(ans)


if __name__ == "__main__":
    main()
