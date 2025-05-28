# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = [[0 for _ in range(n)] for _ in range(n)]
    b = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n - 1):
        ai = list(map(int, input().split()))

        for j, aij in enumerate(ai, i + 1):
            a[i][j] = aij
            a[j][i] = aij

    for i in range(n - 1):
        bi = list(map(int, input().split()))

        for j, bij in enumerate(bi, i + 1):
            b[i][j] = bij
            b[j][i] = bij

    inf = 10**18
    dp = [[[inf] * 2 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            dp[i][j][0] = a[i][j]
            dp[i][j][1] = b[i][j]

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
                    dist[i][j][0] = min(dist[i][j][0], dist[i][k][0] + dist[k][j][0])
                    dist[i][j][1] = min(dist[i][j][1], dist[i][k][0] + dist[k][j][1])
                    dist[i][j][1] = min(dist[i][j][1], dist[i][k][1] + dist[k][j][0])

        return dist

    d = warshall_floyd(dp)

    for i in range(n - 1):
        ans = list()

        for j in range(i + 1, n):
            ans.append(d[i][j][1])

        print(*ans)


if __name__ == "__main__":
    main()
