# -*- coding: utf-8 -*-


def main():
    from bisect import bisect
    import sys

    input = sys.stdin.readline

    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    print(bisect(a, x))


if __name__ == "__main__":
    main()
