# -*- coding: utf-8 -*-


def main():
    from collections import deque

    n = int(input())
    graph = [[] for _ in range(n)]

    # See:
    # https://www.youtube.com/watch?v=26AWkQNRb-A
    # https://atcoder.jp/contests/abc126/submissions/5456359
    for i in range(n - 1):
        ui, vi, wi = map(int, input().split())
        ui -= 1
        vi -= 1
        graph[ui].append((vi, wi))
        graph[vi].append((ui, wi))

    ans = [-1 for _ in range(n)]
    q = deque()
    ans[0] = 0
    q.append(0)

    while q:
        vj = q.popleft()

        for uj, wj in graph[vj]:
            if ans[uj] != -1:
                continue

            ans[uj] = (ans[vj] + wj) % 2
            q.append(uj)

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
