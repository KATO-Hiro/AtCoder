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

    n, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    inf = 10**18

    for i in range(n):
        for j in range(n):
            if a[i][j] == 1:
                continue

            a[i][j] = inf

    dist = warshall_floyd(a)

    q = int(input())

    for _ in range(q):
        si, ti = map(int, input().split())
        si -= 1
        ti -= 1

        si %= n
        ti %= n
        ans = dist[si][ti]

        if ans == inf:
            ans = -1

        print(ans)


if __name__ == "__main__":
    main()
