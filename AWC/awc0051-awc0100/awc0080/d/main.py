# -*- coding: utf-8 -*-


def main():
    import sys
    from atcoder.dsu import DSU

    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    edges = []

    for i in range(m):
        ui, vi, wi = map(int, input().split())
        ui -= 1
        vi -= 1

        edges.append((wi, ui, vi, i + 1))

    e = list(map(int, input().split()))
    f = set([i for i in range(1, m + 1)])
    must = []
    optional = []

    for ei in e:
        if ei in f:
            f.discard(ei)

        must.append(edges[ei - 1])

    for fj in list(f):
        optional.append(edges[fj - 1])

    must.sort()
    optional.sort()

    uf = DSU(n)
    ans = 0

    for wi, ui, vi, i in must:
        if uf.same(ui, vi):
            print(-1)
            exit()

        ans += wi
        uf.merge(ui, vi)

    for wi, ui, vi, i in optional:
        if uf.same(ui, vi):
            continue

        ans += wi
        uf.merge(ui, vi)

    if uf.size(0) != n:
        print(-1)
        exit()

    print(ans)


if __name__ == "__main__":
    main()
