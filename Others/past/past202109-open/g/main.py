# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    abc = [tuple(map(int, input().split())) for _ in range(n)]
    ng, ok = 1, 10**20

    def f(now):
        count = 0

        for ai, bi, ci in abc:
            if now < bi:
                continue

            x = ((now - bi) // ci) + 1
            count += min(x, ai)

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
