# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import pairwise

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))

    for _ in range(n - 1):
        b = []

        for first, second in pairwise(a):
            b.append(first + second)

        print(*b)
        a = b


if __name__ == "__main__":
    main()
