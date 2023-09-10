# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    l = list(map(int, input().split()))

    ng = max(l) - 1
    ok = 10**18

    def f(wj):
        count = 1
        tmp_w = wj

        for li in l:
            if tmp_w - li < 0:
                count += 1
                tmp_w = wj

            tmp_w -= li

            if tmp_w >= 1:
                tmp_w -= 1

        return count <= m

    while abs(ok - ng) > 1:
        wj = (ok + ng) // 2

        if f(wj):
            ok = wj
        else:
            ng = wj

    print(ok)


if __name__ == "__main__":
    main()
