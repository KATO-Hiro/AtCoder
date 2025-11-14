# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    y, b = map(int, input().split())
    print(y * b**2)


if __name__ == "__main__":
    main()
