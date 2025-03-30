# -*- coding: utf-8 -*-


def solve():
    from itertools import pairwise

    n = int(input())
    a = list(map(lambda x: int(x) - 1, input().split()))
    ids = [list() for _ in range(n)]

    # 各ペアのインデックスを管理
    for i, ai in enumerate(a):
        ids[ai].append(i)

    # 隣接している異なるペアの候補を集合で管理
    candidates = set()

    for first, second in pairwise(a):
        # 常に first < second となるようにする
        if first > second:
            first, second = second, first
        # 既に隣同士のペアは候補から除外
        if first == second:
            continue

        candidates.add((first, second))

    ans = 0

    # ペアの候補から条件を満たすものを数える
    for x, y in candidates:
        xl, xr = ids[x][0], ids[x][1]
        yl, yr = ids[y][0], ids[y][1]

        # コーナーケース: x か y が隣同士の場合は除外
        if xl + 1 == xr:
            continue
        if yl + 1 == yr:
            continue
        if abs(xl - yl) == 1 and abs(xr - yr) == 1:
            ans += 1

    print(ans)


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
