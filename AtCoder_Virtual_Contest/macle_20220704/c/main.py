# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, x = map(int, input().split())
    print(b // x - (a - 1) // x)


if __name__ == "__main__":
    main()
