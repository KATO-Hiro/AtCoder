# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    m, a, b = map(int, input().split())
    n = m**2
    graph = [[] for _ in range(n)]

    for x in range(m):
        for y in range(m):
            k = a * y + b * x
            k %= m

            # (i, j) を 1次元で処理
            u = x * m + y
            v = y * m + k
            graph[v].append(u)

    used = [False] * n
    d = deque()

    def push(v):
        if used[v]:
            return

        used[v] = True
        d.append(v)

    for i in range(m):
        push(i)
        push(i * m)

    while d:
        v = d.popleft()

        for to in graph[v]:
            push(to)

    ans = 0

    for used_i in used:
        if used_i:
            continue

        ans += 1

    print(ans)


if __name__ == "__main__":
    main()
