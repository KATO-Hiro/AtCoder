# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = sorted(list(map(int, input().split())))
    b = list(map(int, input().split()))
    inf = 10**18
    ng, ok = -1, inf

    def f(wj):
        nonlocal b

        c = sorted(b + [wj])
        flag = True

        for ai, bi in zip(a, c):
            if ai > bi:
                flag = False
                break

        return flag

    while abs(ok - ng) > 1:
        wj = (ok + ng) // 2

        if f(wj):
            ok = wj
        else:
            ng = wj

    if ok == inf:
        print(-1)
    else:
        print(ok)


if __name__ == "__main__":
    main()
