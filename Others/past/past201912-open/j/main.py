# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    inf = 10**18

    def dijkstra(vertex_count: int, source: int):
        from heapq import heappop, heappush

        hq = [(0, source)]  # weight, vertex number (0-indexed)
        costs = [inf for _ in range(vertex_count)]
        costs[source] = 0
        visited = [False for _ in range(vertex_count)]
        dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
        dxy = dxy[:4]

        while hq:
            cost, vertex = heappop(hq)

            if cost > costs[vertex]:
                continue

            if visited[vertex]:
                continue

            visited[vertex] = True

            for dx, dy in dxy:
                y, x = divmod(vertex, w)
                ny, nx = y + dy, x + dx

                if not (0 <= ny < h and 0 <= nx < w):
                    continue

                new_vertex = ny * w + nx
                new_cost = cost + a[ny][nx]

                if new_cost < costs[new_vertex]:
                    costs[new_vertex] = new_cost
                    heappush(hq, (new_cost, new_vertex))

        return costs

    # See:
    # https://blog.hamayanhamayan.com/entry/2019/12/31/235948
    # 左下x - 右下y - 右上zは、ある1点pを共有したパスになっている
    # x - p、y - p、z - pの最短経路をそれぞれ求める
    dist_x = dijkstra(h * w, (h - 1) * w)
    dist_y = dijkstra(h * w, h * w - 1)
    dist_z = dijkstra(h * w, w - 1)
    ans = inf

    for i in range(h):
        for j in range(w):
            now = i * w + j
            # 頂点pを3回通るので、重複分を除く
            candidate = dist_x[now] + dist_y[now] + dist_z[now] - 2 * a[i][j]

            ans = min(ans, candidate)

    print(ans)


if __name__ == "__main__":
    main()
