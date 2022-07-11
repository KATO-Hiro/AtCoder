# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, x, y = map(int, input().split())
    print(min(x // a, y // b))


if __name__ == "__main__":
    main()
