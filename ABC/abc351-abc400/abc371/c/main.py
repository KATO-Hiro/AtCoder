# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict
    from itertools import permutations

    input = sys.stdin.readline

    n = int(input())
    mg = int(input())
    uv = set()

    for _ in range(mg):
        ui, vi = map(int, input().split())
        ui -= 1
        vi -= 1
        uv.add((ui, vi))

    mh = int(input())
    ab = set()

    for _ in range(mh):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
        ab.add((ai, bi))

    a = defaultdict(int)

    for i in range(n - 1):
        ai = list(map(int, input().split()))

        for j, aij in enumerate(ai, i + 1):
            a[(i, j)] = aij

    # print(a)

    inf = 10**18
    ans = inf

    for pattern in permutations(range(n)):
        cost = 0

        # グラフGのみに存在する場合は、グラフHに辺を追加
        for ui, vi in uv:
            pui, pvi = pattern[ui], pattern[vi]

            if pui > pvi:
                pui, pvi = pvi, pui

            if (pui, pvi) not in ab:
                cost += a[(pui, pvi)]

        # グラフHのみに存在する場合は、グラフHから辺を削除
        for ai, bi in ab:
            index_ai, index_bi = pattern.index(ai), pattern.index(bi)

            if index_ai > index_bi:
                index_ai, index_bi = index_bi, index_ai

            if (index_ai, index_bi) not in uv:
                cost += a[(ai, bi)]

        ans = min(ans, cost)

    print(ans)


if __name__ == "__main__":
    main()
