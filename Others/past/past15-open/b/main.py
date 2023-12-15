# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    c, h = map(int, input().split())

    if h >= 2800:
        print("o")
    else:
        print("x")


if __name__ == "__main__":
    main()
