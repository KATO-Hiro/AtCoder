# -*- coding: utf-8 -*-


def solve():
    n, m, k = map(int, input().split())
    s = input().rstrip()

    graph = [[] for _ in range(n)]

    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append(bi)

    dp = [si == "A" for si in s]

    for _ in range(2 * k):
        ndp = [False] * n

        for cur in range(n):
            for to in graph[cur]:
                if dp[to]:
                    continue

                ndp[cur] = True

        dp = ndp

    if dp[0]:
        print("Alice")
    else:
        print("Bob")


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
