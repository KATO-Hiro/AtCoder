# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n, d = map(int, input().split())
    d = d**2
    xy = [tuple(map(int, input().split())) for _ in range(n)]
    inf = 10**12
    dist = [[inf for _ in range(n)] for _ in range(n)]

    for i in range(n):
        xi, yi = xy[i]

        for j in range(n):
            xj, yj = xy[j]
            di = (xj - xi) ** 2 + (yj - yi) ** 2
            dist[i][j] = di
            dist[j][i] = di

    ans = [False] * n
    q = deque([0])

    while q:
        cur = q.popleft()

        if ans[cur]:
            continue

        ans[cur] = True

        for i, to in enumerate(dist[cur]):
            if ans[i]:
                continue

            if to <= d:
                q.append(i)

    for ans_i in ans:
        if ans_i:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
