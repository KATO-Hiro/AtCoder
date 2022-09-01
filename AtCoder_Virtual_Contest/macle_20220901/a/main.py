# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, p = map(int, input().split())
    p += a * 3
    p //= 2

    print(p)


if __name__ == "__main__":
    main()
