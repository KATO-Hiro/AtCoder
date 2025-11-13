# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, b = map(int, input().split())
    print(max(0, h - b))


if __name__ == "__main__":
    main()
