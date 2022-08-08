# -*- coding: utf-8 -*-


def main():
    from itertools import combinations
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())

    for pattern in combinations(range(1, m + 1), n):
        print(*pattern)


if __name__ == "__main__":
    main()
