# -*- coding: utf-8 -*-


def warshall_floyd(dist):
    """
    Args:
        Distance matrix between two points.

    Returns:
        Matrix of shortest distance.

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

    h, w = map(int, input().split())
    c = [list(map(int, input().split())) for _ in range(10)]
    a = [list(map(int, input().split())) for _ in range(h)]

    # 壁に書かれている数字を1にする操作 = 有向グラフの問題と捉える
    # 操作回数の最小化 = 全頂点に対する最短経路問題に帰着 = WF法
    # cost[x][1]
    costs = warshall_floyd(c)
    cost = [cost[1] for cost in costs]
    # print(costs)
    # print(cost)

    ans = 0

    for i in range(h):
        for j in range(w):
            if a[i][j] == -1:
                continue

            ans += cost[a[i][j]]

    print(ans)


if __name__ == "__main__":
    main()
