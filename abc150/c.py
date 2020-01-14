# -*- coding: utf-8 -*-


def main():
    from itertools import permutations

    n = int(input())
    p = tuple(map(int, input().split()))
    q = tuple(map(int, input().split()))
    a = 0
    b = 0

    ps = sorted((permutations(range(1, n + 1))))

    for index, pi in enumerate(ps, 1):
        if pi == p:
            a = index
        if pi == q:
            b = index

    print(abs(a - b))


if __name__ == '__main__':
    main()
