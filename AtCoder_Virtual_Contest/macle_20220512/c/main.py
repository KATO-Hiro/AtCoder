# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    from collections import deque
    import sys

    input = sys.stdin.readline

    n = int(input())
    graph = [[] for _ in range(n)]
    edges = defaultdict()
    
    for i in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
    
        graph[ai].append(bi)
        graph[bi].append(ai)
        edges[(ai, bi)] = i
        edges[(bi, ai)] = i

    d = deque()
    d.append((0, 0))
    visited = [False for _ in range(n)]
    ans = [0] * (n - 1)

    while d:
        vertex, color_id = d.popleft()

        if visited[vertex]:
            continue

        visited[vertex] = True
        id = 1

        for to in graph[vertex]:
            if visited[to]:
                continue

            if id == color_id:
                id += 1

            d.append((to, id))
            ans[edges[(to, vertex)]] = id
            id += 1
    
    print(max(ans))
    print(*ans, sep='\n')


if __name__ == "__main__":
    main()
