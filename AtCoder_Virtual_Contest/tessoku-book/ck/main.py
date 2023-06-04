# -*- coding: utf-8 -*-


def f(value, n):
    return value**3 + value <= n


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ok = 0
    ng = n

    while ng - ok > 10 ** (-10):
        wj = (ok + ng) / 2

        if f(wj, n):
            ok = wj
        else:
            ng = wj

    print(ok)


if __name__ == "__main__":
    main()
