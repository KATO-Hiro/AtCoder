# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x, y = map(int, input().split())

    if x == y:
        print(x)
    else:
        print(3 - x - y)


if __name__ == "__main__":
    main()
