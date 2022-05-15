# -*- coding: utf-8 -*-


def main():
    from itertools import combinations
    import sys

    input = sys.stdin.readline

    n, w = map(int, input().split())
    a = list(map(int, input().split()))

    c2 = list(combinations(a, 2))
    c3 = list(combinations(a, 3))

    ans = set()

    for ai in a:
        if ai <= w:
            ans.add(ai)
    
    for a1, a2 in c2:
        if (a1 + a2) <= w:
            ans.add(a1 + a2)

    for a1, a2, a3 in c3:
        if (a1 + a2 + a3) <= w:
            ans.add(a1 + a2 + a3)
    
    print(len(ans))


if __name__ == "__main__":
    main()
