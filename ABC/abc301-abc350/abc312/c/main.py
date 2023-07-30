# -*- coding: utf-8 -*-


def f(wj, a):
    count = 0

    for ai in a:
        if wj >= ai:
            count += 1

    return count


def g(wj, b):
    count = 0

    for bi in b:
        if wj <= bi:
            count += 1

    return count


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ng = 0
    ok = 10**9 + 1

    while ok - ng > 1:
        wj = (ok + ng) // 2

        if f(wj, a) >= g(wj, b):
            ok = wj
        else:
            ng = wj

    print(ok)


if __name__ == "__main__":
    main()
