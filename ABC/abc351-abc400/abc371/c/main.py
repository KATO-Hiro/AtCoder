# -*- coding: utf-8 -*-


def read_graph(n):
    from collections import defaultdict

    m = int(input())
    g = defaultdict(bool)

    for i in range(n):
        for j in range(n):
            g[(i, j)] = False

    for _ in range(m):
        ui, vi = map(int, input().split())
        ui -= 1
        vi -= 1

        g[(ui, vi)] = True
        g[(vi, ui)] = True

    return g


def main():
    import sys
    from collections import defaultdict
    from itertools import permutations

    input = sys.stdin.readline

    n = int(input())
    g = read_graph(n)
    h = read_graph(n)

    a = defaultdict(int)

    for i in range(n - 1):
        ai = list(map(int, input().split()))

        for j, aij in enumerate(ai, i + 1):
            a[(i, j)] = aij
            a[(j, i)] = aij

    inf = 10**18
    ans = inf

    for pattern in permutations(range(n)):
        cost = 0

        for i in range(n):
            for j in range(i + 1, n):
                if h[(i, j)] != g[(pattern[i], pattern[j])]:
                    cost += a[(i, j)]

        ans = min(ans, cost)

    print(ans)


if __name__ == "__main__":
    main()
