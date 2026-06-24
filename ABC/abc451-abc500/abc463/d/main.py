# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import pairwise

    input = sys.stdin.readline

    n, k = map(int, input().split())
    lr = [tuple(map(int, input().split())) for _ in range(n)]
    lr.sort(key=lambda x: x[1])

    inf = 10**18
    ok, ng = 0, inf

    def f(w):
        r_max = -inf
        count = 0

        for li, ri in lr:
            if li >= r_max:
                r_max = ri + w
                count += 1

        return count >= k

    while abs(ng - ok) > 1:
        wj = (ok + ng) // 2

        if f(wj):
            ok = wj
        else:
            ng = wj

    if ok == 0:
        ok = -1

    print(ok)


if __name__ == "__main__":
    main()
