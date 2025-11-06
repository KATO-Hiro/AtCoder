# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x = int(input())
    y = int(input())
    z = int(input())

    if z >= min(x, y):
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    main()
