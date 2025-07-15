# -*- coding: utf-8 -*-


def solve():
    n = int(input())
    p = list(map(int, input().split()))
    q = sorted(p)

    ans = 2

    if p == q:
        ans = 0
    elif p[0] == n and p[-1] == 1:
        ans = 3
    else:
        p_max = 0

        for i, pi in enumerate(p, 1):
            if pi == i and p_max == i - 1:
                ans = 1
                break

            p_max = max(p_max, pi)

    print(ans)


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
