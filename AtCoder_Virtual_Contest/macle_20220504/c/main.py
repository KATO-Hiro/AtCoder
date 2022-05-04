# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    t = list(map(int, input().split()))
    total = sum(t)
    m = 10 ** 5 + 10
    inf = 10 ** 9
    dp = [inf for _ in range(m)]
    dp[0] = 0

    # See:
    # https://blog.hamayanhamayan.com/entry/2021/06/07/024420
    for i in range(n):
        ndp = [inf for _ in range(m)]

        for j in range(m):
            if dp[j] != inf:
                # use 1st
                ndp[j + t[i]] = min(ndp[j + t[i]], dp[j])

                # use 2nd
                ndp[j] = min(ndp[j], dp[j] + t[i])

        dp = ndp
    
    ans = float("inf")
    
    for d in dp:
        ans = min(ans, max(d, total - d))

    print(ans)


if __name__ == "__main__":
    main()
