# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import pairwise

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    used = False

    for ai, aj in pairwise(a):
        if used:
            used = False
            continue

        if ai == k:
            used = False
            ans += 1
        elif aj == k:
            used = True
            ans += 1

        if ai > aj:
            ai, aj = aj, ai
        if ai < k < aj:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
