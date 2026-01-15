# -*- coding: utf-8 -*-


def solve():
    n, a, b = map(int, input().split())

    if n < b:
        print(0)
        return

    ok, ng = 0, 10**12

    def f(wj):
        return (a * wj * (wj - 1) // 2) + (b * wj) <= n

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

    q = int(input())

    for _ in range(q):
        solve()


if __name__ == "__main__":
    main()
