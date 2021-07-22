# -*- coding: utf-8 -*-


def warshall_floyd(dist):
    v_count = len(dist[0])

    for k in range(v_count):
        for i in range(v_count):
            for j in range(v_count):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    inf = 10 ** 18
    graph = [[inf for _ in range(n)] for _ in range(n)]
    edges = []

    for i in range(n):
        graph[i][i] = 0
    
    for _ in range(m):
        ai, bi, ci = map(int, input().split())
        ai -= 1
        bi -= 1
    
        graph[ai][bi] = ci
        graph[bi][ai] = ci
        edges.append((ai, bi, ci))
    
    d = warshall_floyd(graph)

    ans = 0

    for ai, bi, ci in edges:
        if graph[ai][bi] != ci:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
