# -*- coding: utf-8 -*-

inf = 10**18


def f(wj, n, ratio):
    m = str(wj) * ratio
    m = int(m)

    if m > inf:
        return False

    return m <= n


def solve():
    n = int(input())
    ans = 11

    for ratio in range(2, 18 + 1):
        ok, ng = 1, 10**9 + 1

        while abs(ok - ng) > 1:
            wj = (ok + ng) // 2

            if f(wj, n, ratio):
                ok = wj
            else:
                ng = wj

        candidate = str(ok) * ratio
        candidate = int(candidate)

        if candidate > n:
            continue

        ans = max(ans, candidate)

    print(ans)


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
