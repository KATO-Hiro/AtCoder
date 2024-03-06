# -*- coding: utf-8 -*-


def main():
    import sys
    from math import lcm

    input = sys.stdin.readline

    n, m, k = map(int, input().split())

    # k番目の数を決め打ちして、二分探索
    ng, ok = 0, 10**20

    def f(wj):
        count = wj // n
        count += wj // m
        count -= wj // lcm(n, m) * 2

        return count >= k

    while abs(ok - ng) > 1:
        wj = (ok + ng) // 2

        if f(wj):
            ok = wj
        else:
            ng = wj

    print(ok)


if __name__ == "__main__":
    main()
