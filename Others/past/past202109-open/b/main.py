# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))

    c = a & b
    print(' '.join(map(str, sorted(c))))


if __name__ == "__main__":
    main()
