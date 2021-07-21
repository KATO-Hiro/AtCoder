# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    edges = list()
    inf = 10 ** 18
    ans = 0

    for i in range(n):
        for j in range(i + 1, n):
            edges.append((a[i][j], (i, j)))
            ans += a[i][j]
    
    for dist, (i, j) in sorted(edges, reverse=True):
        if a[i][j] == inf:
            continue
    
        for k in range(n):
            if (k != i and k != j) and(a[i][k] != inf and a[k][j] != inf):
                if a[i][k] + a[k][j] == a[i][j]:
                    ans -= dist
                    a[i][j] = inf
                    a[j][i] = inf
                    break
                elif a[i][k] + a[k][j] < a[i][j]:
                    print(-1)
                    exit()

    print(ans)


if __name__ == "__main__":
    main()

