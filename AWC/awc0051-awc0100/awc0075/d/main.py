# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    inf = 10**12
    ng, ok = -1, inf

    def f(x):
        count = 0
        tmp = []

        for ai in a:
            if len(tmp) == 0:
                tmp.append(ai)
                count += 1
            elif len(tmp) < m and ai <= tmp[0] + x:
                tmp.append(ai)
            else:
                tmp = []
                tmp.append(ai)
                count += 1

        return count <= k

    while abs(ok - ng) > 1:
        wj = (ok + ng) // 2

        if f(wj):
            ok = wj
        else:
            ng = wj

    print(ok)


if __name__ == "__main__":
    main()
