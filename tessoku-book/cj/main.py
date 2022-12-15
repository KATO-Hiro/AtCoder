# -*- coding: utf-8 -*-


def main():
    from bisect import bisect_right
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = sorted(list(map(int, input().split())))
    q = int(input())

    for _ in range(q):
        xi = int(input())
        index = bisect_right(a, xi - 1)
        print(index)


if __name__ == "__main__":
    main()
