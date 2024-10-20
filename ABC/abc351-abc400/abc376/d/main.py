# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        if bi == 0:
            bi = n

        graph[ai].append(bi)

    inf = 10**9
    q = deque([0])
    # 頂点1に戻る = 超頂点に戻ると言い換え
    dist = [inf] * (n + 1)
    dist[0] = 0

    while q:
        cur = q.popleft()

        for to in graph[cur]:
            if dist[to] != inf:
                continue

            dist[to] = dist[cur] + 1
            q.append((to))

    ans = dist[n]

    if ans == inf:
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    main()
