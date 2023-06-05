# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ng = 0
    ok = 10**9 + 1

    def f(wj):
        count = 0

        for ai in a:
            count += wj // ai

        return count >= k

    while ok - ng > 1:
        wj = (ok + ng) // 2

        if f(wj):
            ok = wj
        else:
            ng = wj

    print(ok)


if __name__ == "__main__":
    main()
