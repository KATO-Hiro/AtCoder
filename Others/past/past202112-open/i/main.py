# -*- coding: utf-8 -*-


def compress_coordinate(elements: list) -> dict:
    """Means that reduce the numerical value while maintaining the magnitude
        relationship.

    Args:
        elements: list of integer numbers (greater than -1).

    Returns:
        A dictionary's items ((original number, compressed number) pairs).

    Landau notation: O(n log n)
    """

    # See:
    # https://atcoder.jp/contests/abc036/submissions/5707999?lang=ja
    compressed_list = sorted(set(elements))
    return {element: index for index, element in enumerate(compressed_list)}


def dijkstra(vertex_count: int, source: int, edges):
    """Uses Dijkstra's algorithm to find the shortest path in a graph.

    Args:
        vertex_count: The number of vertices.
        source      : Vertex number (0-indexed).
        edges       : List of (cost, edge) (0-indexed).

    Returns:
        costs  : List of the shortest distance.
        parents: List of parent vertices.

    Landau notation: O(|Edges|log|Vertices|).

    See:
    https://atcoder.jp/contests/abc191/submissions/19964078
    https://atcoder.jp/contests/abc191/submissions/19966232
    """

    from heapq import heappop, heappush

    hq = [(0, source)]  # weight, vertex number (0-indexed)
    costs = [float("inf") for _ in range(vertex_count)]
    costs[source] = 0
    visited = [False for _ in range(vertex_count)]
    pending = -1
    parents = [pending for _ in range(vertex_count)]

    while hq:
        cost, vertex = heappop(hq)

        if cost > costs[vertex]:
            continue

        if visited[vertex]:
            continue

        visited[vertex] = True

        for weight, edge in edges[vertex]:
            new_cost = cost + weight

            if new_cost < costs[edge]:
                costs[edge] = new_cost
                parents[edge] = vertex
                heappush(hq, (new_cost, edge))

    return costs, parents


def main():
    import sys
    from itertools import pairwise

    input = sys.stdin.readline

    n, m = map(int, input().split())
    nodes = [0, n - 1]
    abc = list()

    for _ in range(m):
        ai, bi, ci = map(int, input().split())
        ai -= 1
        bi -= 1

        nodes.append(ai)
        nodes.append(bi)

        abc.append((ai, bi, ci))

    compressed = compress_coordinate(nodes)
    size = len(compressed)
    graph = [[] for _ in range(size)]

    for i, j in pairwise(compressed.keys()):
        di, dj = compressed[i], compressed[j]
        d = j - i

        graph[di].append((d, dj))
        graph[dj].append((d, di))

    for ai, bi, ci in abc:
        cai, cbi = compressed[ai], compressed[bi]

        graph[cai].append((ci, cbi))
        graph[cbi].append((ci, cai))

    costs, _ = dijkstra(size, 0, graph)
    print(costs[-1])


if __name__ == "__main__":
    main()
