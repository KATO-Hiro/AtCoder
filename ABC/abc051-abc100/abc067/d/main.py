# -*- coding: utf-8 -*-


def calc_dist(n, source, graph):
    from collections import deque

    dist = [0 for _ in range(n)]
    d = deque()
    d.append(source)
    visited = [False for _ in range(n)]
    visited[source] = True

    while d:
        di = d.popleft()

        for g in graph[di]:
            if visited[g]:
                continue

            visited[g] = True
            dist[g] = dist[di] + 1
            d.append(g)

    return dist


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    graph = [[] for _ in range(n)]

    for _ in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append(bi)
        graph[bi].append(ai)

    dist1 = calc_dist(n, 0, graph)
    dist2 = calc_dist(n, n - 1, graph)

    f_count = 0
    s_count = 0

    for fi, si in zip(dist1, dist2):
        if fi <= si:
            f_count += 1
        else:
            s_count += 1

    if f_count > s_count:
        print("Fennec")
    else:
        print("Snuke")


if __name__ == "__main__":
    main()
