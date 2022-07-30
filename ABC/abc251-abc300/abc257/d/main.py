# -*- coding: utf-8 -*-


def warshall_floyd(dist):
    '''
        Args:
            Distance matrix between two points.
        Returns:
            Matrix of shortest distance.
        Landau notation: O(n ** 3).
    '''

    v_count = len(dist[0])

    for k in range(v_count):
        for i in range(v_count):
            for j in range(v_count):
                dist[i][j] = min(dist[i][j], max(dist[i][k], dist[k][j]))

    return dist


def main():
    from math import ceil
    import sys

    input = sys.stdin.readline

    n = int(input())
    op = [[0] * n for _ in range(n)]
    xyp = [tuple(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        xi, yi, pi = xyp[i]

        for j in range(n):
            xj, yj, _ = xyp[j]
            
            dist = abs(xi - xj) + abs(yi - yj)
            op[i][j] = ceil(dist / pi)

    results = warshall_floyd(op)
    ans = float('inf')

    for result in results:
        ans = min(ans, max(result))

    print(ans)


if __name__ == "__main__":
    main()
