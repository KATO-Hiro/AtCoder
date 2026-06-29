# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    graph = [[] for _ in range(n)]

    for _ in range(m):
        ai, bi, wi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append((wi, bi))
        graph[bi].append((wi, ai))

    ans = 0

    for i in range(n):
        ti = 0

        for wi, to in graph[i]:
            ti += wi

        if ti < s[i]:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
