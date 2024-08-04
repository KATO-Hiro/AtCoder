# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    inf = 10**20
    ok, ng = 0, inf

    def f(wj):
        total = 0

        for ai in a:
            total += min(ai, wj)

        return total <= m

    while abs(ok - ng) > 1:
        wj = (ok + ng) // 2

        if f(wj):
            ok = wj
        else:
            ng = wj

    if ok != inf - 1:
        ans = ok
    else:
        ans = "infinite"

    print(ans)


if __name__ == "__main__":
    main()
