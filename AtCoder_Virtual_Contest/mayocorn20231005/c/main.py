# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ng, ok = 0, 10**18

    def f(wj):
        sell_count, buy_count = 0, 0

        for ai in a:
            if wj >= ai:
                sell_count += 1
        for bi in b:
            if wj <= bi:
                buy_count += 1

        return sell_count >= buy_count

    while abs(ok - ng) > 1:
        wj = (ok + ng) // 2

        if f(wj):
            ok = wj
        else:
            ng = wj

    print(ok)


if __name__ == "__main__":
    main()
