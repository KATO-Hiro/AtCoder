# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    ok, ng = 1, 10**18

    def f(x):
        total, count = 0, 0

        for ai in a:
            total += ai

            if total >= x:
                count += 1
                total = 0

        return count >= k

    while abs(ng - ok) > 1:
        wj = (ok + ng) // 2

        if f(wj):
            ok = wj
        else:
            ng = wj

    print(ok)


if __name__ == "__main__":
    main()
