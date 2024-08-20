# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import product

    input = sys.stdin.readline

    n, k = map(int, input().split())
    r = list(map(int, input().split()))
    a = [range(1, ri + 1) for ri in r]

    for pi in product(*a):
        if sum(pi) % k == 0:
            print(*pi)


if __name__ == "__main__":
    main()
