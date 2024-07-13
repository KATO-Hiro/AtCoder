# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate, pairwise

    input = sys.stdin.readline

    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    dists = [0] * (n + 1)

    # [frm, to)
    def add(frm, to, dist):
        dists[frm] += dist
        dists[to] -= dist

    # 各区間で独立に考える
    for frm, to in pairwise(x):
        if frm > to:
            frm, to = to, frm

        dist1 = to - frm
        dist2 = n - dist1

        add(0, frm, dist1)
        add(frm, to, dist2)
        add(to, n, dist1)

    dists_acc = list(accumulate(dists))
    ans = min(dists_acc[:n])
    print(ans)


if __name__ == "__main__":
    main()
