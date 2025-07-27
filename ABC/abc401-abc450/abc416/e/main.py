# -*- coding: utf-8 -*-


def warshall_floyd(dist):
    """
    Args:
        dist (list[list[int]]): A 2D matrix where dist[i][j] represents the distance 
            from vertex i to vertex j in a graph. If there is no direct edge between 
            i and j, dist[i][j] should be set to a very large value (e.g., infinity).

    Returns:
        list[list[int]]: The updated 2D matrix where dist[i][j] contains the shortest 
            distance from vertex i to vertex j. The input matrix is modified in place.

    Landau notation: O(n ** 3).
    """

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
    inf = 10**18
    graph = [[inf for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        graph[i][i] = 0

    for _ in range(m):
        ai, bi, ci = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai][bi] = min(graph[ai][bi], ci)
        graph[bi][ai] = min(graph[bi][ai], ci)

    k, t = map(int, input().split())
    d = list(map(int, input().split()))

    # 超頂点を導入
    # 空港diから超頂点nへの辺をコストt、nから別の空港への辺をコスト0とする
    for di in d:
        di -= 1
        graph[di][n] = t
        graph[n][di] = 0

    dist = warshall_floyd(graph)

    q = int(input())

    for _ in range(q):
        query = list(map(int, input().split()))

        if query[0] == 1:
            xi, yi, ti = query[1:]
            xi -= 1
            yi -= 1

            for i in range(n + 1):
                for j in range(n + 1):
                    dist1 = dist[i][xi] + ti + dist[yi][j]
                    dist2 = dist[i][yi] + ti + dist[xi][j]
                    dist[i][j] = min(dist[i][j], dist1, dist2)
        elif query[0] == 2:
            xi = query[1] - 1

            for i in range(n + 1):
                for j in range(n + 1):
                    dist1 = dist[i][xi] + t + dist[n][j]
                    dist2 = dist[i][n] + 0 + dist[xi][j]
                    dist[i][j] = min(dist[i][j], dist1, dist2)
        else:
            ans = 0

            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    if dist[i][j] == inf:
                        continue

                    ans += dist[i][j]

            print(ans)


if __name__ == "__main__":
    main()
