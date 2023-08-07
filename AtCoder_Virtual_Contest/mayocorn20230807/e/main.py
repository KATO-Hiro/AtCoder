# -*- coding: utf-8 -*-


def main():
    import sys
    from math import ceil

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())), reverse=True)
    ng, ok = -1, 10**18 + 1

    if sum(a) <= k:
        print(0)
        exit()

    def f(wj):
        count = 0

        for ai, bi in zip(a, b):
            # 操作が不要なケースを考慮
            count += ceil(max(0, (ai * bi - wj)) / bi)

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
