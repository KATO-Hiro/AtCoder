# -*- coding: utf-8 -*-


def dijkstra(vertex_count: int, edges, ph):
    from heapq import heappop, heappush

    hq = []  # weight, vertex number (0-indexed)
    pending = -1
    dists = [pending for _ in range(vertex_count)]

    for pi, hi in ph:
        pi -= 1
        hq.append((-hi, pi))
        dists[pi] = hi

    while hq:
        dist, vertex = heappop(hq)
        dist *= -1

        if dist != dists[vertex]:
            continue

        for edge in edges[vertex]:
            new_dist = dist - 1

            if dists[edge] >= new_dist:
                continue

            dists[edge] = new_dist
            heappush(hq, (-new_dist, edge))

    return dists


def main():
    import sys

    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append(bi)
        graph[bi].append(ai)

    ph = [tuple(map(int, input().split())) for _ in range(k)]
    dist = dijkstra(vertex_count=n, edges=graph, ph=ph)

    ans = [i for i, di in enumerate(dist, 1) if di >= 0]

    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    main()
