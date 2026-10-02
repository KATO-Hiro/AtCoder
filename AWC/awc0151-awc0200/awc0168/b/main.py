# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    d = list(map(int, input().split()))
    sum_d = sum(d)
    ng, ok = 0, 10**18

    def f(day):
        return m * day >= sum_d

    while abs(ok - ng) > 1:
        wj = (ok + ng) // 2

        if f(wj):
            ok = wj
        else:
            ng = wj

    print(ok)


if __name__ == "__main__":
    main()
