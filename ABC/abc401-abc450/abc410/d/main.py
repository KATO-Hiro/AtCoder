# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n, m = map(int, input().split())
    w_max = 1 << 10
    graph = [[] for _ in range(n * w_max)]

    for _ in range(m):
        ai, bi, wi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append((wi, bi))

    # 頂点倍加(頂点、現時点のxor)
    q = deque()
    visited = [False] * (n * w_max)

    def push(vertex, x):
        nv = vertex * w_max + x

        if visited[nv]:
            return

        visited[nv] = True
        q.append(nv)

    push(0, 0)

    while q:
        qi = q.popleft()
        vi, x = divmod(qi, w_max)

        for wi, to in graph[vi]:
            push(to, x ^ wi)

    for j in range(w_max):
        x = (n - 1) * w_max + j

        if visited[x]:
            print(j)
            exit()

    print(-1)


if __name__ == "__main__":
    main()
