# -*- coding: utf-8 -*-


def main():
    from itertools import permutations
    import sys

    input = sys.stdin.readline

    n = int(input())
    p = tuple(map(int, input().split()))
    q = tuple(map(int, input().split()))
    ps = list()

    for pi in permutations(range(1, n + 1), n):
        ps.append(pi)
    
    a = b = 0
    
    for i, pi in enumerate(ps, 1):
        if pi == p:
            a = i
        if pi == q:
            b = i

    print(abs(a - b))


if __name__ == "__main__":
    main()
