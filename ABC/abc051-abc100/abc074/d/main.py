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
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    b = [ai[:] for ai in a]
    dist = warshall_floyd(b)
    ans = 0

    for i in range(n):
        for j in range(i + 1, n):
            if a[i][j] != dist[i][j]:
                print(-1)
                exit()

    for i in range(n):
        for j in range(i + 1, n):
            is_need = True

            for k in range(n):
                if k == i or k == j:
                    continue

                if dist[i][j] ==  dist[i][k] + dist[k][j]:
                    is_need = False
            
            if is_need:
                ans += dist[i][j]

    print(ans)


if __name__ == "__main__":
    main()

