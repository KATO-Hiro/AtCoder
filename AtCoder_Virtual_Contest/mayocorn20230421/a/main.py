# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, a, b = map(int, input().split())
    print(min(a * n, b))


if __name__ == "__main__":
    main()
