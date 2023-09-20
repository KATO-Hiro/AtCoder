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
        remain = wj

        for li in l:
            if li > remain:
                count += 1
                remain = wj

            remain -= li

            if remain > 0:
                remain -= 1

        return count

    while ok - ng > 1:
        wj = (ok + ng) // 2

        if f(wj) <= m:
            ok = wj
        else:
            ng = wj

    print(ok)


if __name__ == "__main__":
    main()
