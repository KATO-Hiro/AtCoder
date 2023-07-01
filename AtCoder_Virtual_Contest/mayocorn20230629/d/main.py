# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    graph = [[] for _ in range(n)]

    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append(bi)

    inf = 10**18
    dp = [inf] * n
    ans = -inf

    for i in range(n):
        ans = max(ans, a[i] - dp[i])

        for j in graph[i]:
            dp[j] = min(dp[j], dp[i], a[i])

    print(ans)


if __name__ == "__main__":
    main()
