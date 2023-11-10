# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m, d = map(int, input().split())
    xv = list()

    for _ in range(n):
        xi, vi = map(int, input().split())
        xv.append((xi, vi))

    xv.sort()

    # print(xv)

    inf = 10**12
    ok = -1
    ng = inf

    def f(wj):
        count = 0
        prev = -inf

        for xi, vi in xv:
            if (xi - prev) >= d and (vi >= wj):
                count += 1
                prev = xi

        if count >= m:
            return True
        else:
            return False

    while abs(ng - ok) > 1:
        wj = (ok + ng) // 2

        if f(wj):
            ok = wj
        else:
            ng = wj

    print(ok)


if __name__ == "__main__":
    main()
