# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    l, r = map(int, input().split())
    print(r - l + 1)


if __name__ == "__main__":
    main()
