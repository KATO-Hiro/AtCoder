# -*- coding: utf-8 -*-


def solve():
    na, nb, nc = map(int, input().split())
    ng, ok = 10**9 + 1, 0

    def f(wj):
        if na < wj:
            return False
        if nc < wj:
            return False

        total = na + nc - 2 * wj + nb

        return total >= wj

    while abs(ok - ng) > 1:
        wj = (ok + ng) // 2

        if f(wj):
            ok = wj
        else:
            ng = wj

    print(ok)


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
