# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    for ai in a:
        p, q = divmod(ai, m)
        print(p, q)


if __name__ == "__main__":
    main()
