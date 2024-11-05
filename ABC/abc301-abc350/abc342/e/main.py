# -*- coding: utf-8 -*-


def main():
    import sys
    from heapq import heappop, heappush

    input = sys.stdin.readline

    n, m = map(int, input().split())
    edges = [[] for _ in range(n)]

    for _ in range(m):
        li, di, ki, ci, to, bi = map(int, input().split())
        to -= 1
        bi -= 1

        # 頂点Nから見るため、逆向きに辺を張る
        edges[bi].append((to, li, di, ki, ci))

    inf = 10**19
    hq = [(-inf, n - 1)]  # weight, vertex number (0-indexed)
    ts = [-inf] * n
    ts[-1] = inf

    while hq:
        ti, vertex = heappop(hq)
        ti = -ti

        if ti != ts[vertex]:
            continue

        for to, li, di, ki, ci in edges[vertex]:
            nt = ti - ci

            if li > nt:
                continue

            k_candidate = (nt - li) // di
            k_candidate = min(k_candidate, ki - 1)
            new_cost = li + k_candidate * di

            if new_cost <= ts[to]:
                continue

            ts[to] = new_cost
            heappush(hq, (-new_cost, to))

    for ti in ts[:-1]:
        if ti == -inf:
            ti = "Unreachable"

        print(ti)


if __name__ == "__main__":
    main()
