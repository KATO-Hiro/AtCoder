# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m, l, s, t = map(int, input().split())
    graph = [[] for _ in range(n)]

    for i in range(m):
        ai, bi, ci = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append((bi, ci))

    # (next node, total cost)
    costs = [(0, 0)]

    for _ in range(l):
        ncosts = []

        while costs:
            cur, cost = costs.pop()

            for to, add in graph[cur]:
                ncosts.append((to, cost + add))

        costs = ncosts

    ans = set()

    for i, cost in costs:
        if not (s <= cost <= t):
            continue

        ans.add(i + 1)

    ans = sorted(ans)
    print(*ans)


if __name__ == "__main__":
    main()
