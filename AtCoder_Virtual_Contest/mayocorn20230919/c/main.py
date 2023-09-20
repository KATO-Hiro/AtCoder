# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n = int(input())
    graph = [[] for _ in range(n + 1)]
    costs = [0] * (n + 1)

    for i in range(1, n + 1):
        ti, ki, *ai = map(int, input().split())

        if ki == 0:
            graph[i].append(0)
        else:
            for aij in ai:
                graph[i].append(aij)

        costs[i] = ti

    d = deque([n])
    used = [False] * (n + 1)

    while d:
        cur = d.popleft()

        if used[cur]:
            continue

        used[cur] = True

        for to in sorted(graph[cur], reverse=True):
            if used[to]:
                continue

            d.append(to)

    # print(used)
    ans = 0

    for use, cost in zip(used, costs):
        if use:
            ans += cost

    print(ans)


if __name__ == "__main__":
    main()
