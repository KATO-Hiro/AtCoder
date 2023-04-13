# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline
    
    n = int(input())
    a = list(map(int, input().split()))
    s = [list(input().rstrip()) for _ in range(n)]
    inf = 10 ** 15
    p = [[(inf, 0) for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if s[i][j] == "Y":
                p[i][j] = (1, -a[j])
    
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
                    (dist_ik, value_ik), (dist_kj, value_kj) = dist[i][k], dist[k][j]
                    dist[i][j] = min(dist[i][j], (dist_ik + dist_kj, value_ik + value_kj))

        return dist
    
    results = warshall_floyd(p)
    q = int(input())

    for _ in range(q):
        ui, vi = map(int, input().split())
        ui -= 1
        vi -= 1

        dist, value_max = results[ui][vi]

        if dist == inf:
            print("Impossible")
        else:
            print(dist, a[ui] - value_max)


if __name__ == "__main__":
    main()
