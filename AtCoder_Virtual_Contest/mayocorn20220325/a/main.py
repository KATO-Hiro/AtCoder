# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    print(min(a, b) + min(c, d))


if __name__ == "__main__":
    main()
