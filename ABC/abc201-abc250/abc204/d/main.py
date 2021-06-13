# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    t = list(map(int, input().split()))
    m = 10 ** 5 + 1
    dp = [False for _ in range(m)]
    dp[0] = True

    for ti in t:
        for i in reversed(range(m - ti)):
            dp[i + ti] |= dp[i]

    total = sum(t)
    ans = float("inf")

    for t in range(m):
        if dp[t]:
            ans = min(ans, max(t, total - t))

    print(ans)


if __name__ == "__main__":
    main()
