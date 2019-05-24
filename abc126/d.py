# -*- coding: utf-8 -*-


def main():
    from collections import deque

    n = int(input())
    to = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]

    # See:
    # https://www.youtube.com/watch?v=26AWkQNRb-A
    for i in range(n - 1):
        ui, vi, wi = map(int, input().split())
        ui -= 1
        vi -= 1
        to[ui].append(vi)
        to[vi].append(ui)
        cost[ui].append(wi)
        cost[vi].append(wi)

    ans = [-1 for _ in range(n)]
    q = deque()
    ans[0] = 0
    q.append(0)

    while q:
        vj = q.popleft()

        for j in range(len(to[vj])):
            uj = to[vj][j]
            wj = cost[vj][j]

            if ans[uj] != -1:
                continue

            ans[uj] = (ans[vj] + wj) % 2
            q.append(uj)

    for a in ans:
        print(a)


if __name__ == '__main__':
    main()
