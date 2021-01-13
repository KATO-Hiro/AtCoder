# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    graph = [[] for _ in range(n + 10)]

    for _ in range(m):
        xi, yi = map(int, input().split())
        xi -= 1
        yi -= 1

        graph[xi].append(yi)

    dp = [float("inf") for _ in range(n + 10)]
    ans = -float("inf")

    for i in range(n):
        ans = max(ans, a[i] - dp[i])

        for j in graph[i]:
            dp[j] = min(dp[j], dp[i], a[i])

    print(ans)


if __name__ == "__main__":
    main()
