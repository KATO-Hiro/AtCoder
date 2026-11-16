# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    b, r = map(int, input().split())
    print((30 - b) * (30 - r))


if __name__ == "__main__":
    main()
