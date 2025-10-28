# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b = map(int, input().split())

    if b * 3 < a:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    main()
