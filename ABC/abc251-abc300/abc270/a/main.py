# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b = map(int, input().split())
    print(a | b)


if __name__ == "__main__":
    main()
