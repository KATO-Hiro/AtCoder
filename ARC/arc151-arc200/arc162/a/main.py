# -*- coding: utf-8 -*-


def solve():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0

    for i, pi in enumerate(p, 1):
        ok = True

        for j, pj in enumerate(p, 1):
            if i < j and pi > pj:
                ok = False
                break

        if ok:
            ans += 1

    print(ans)


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
