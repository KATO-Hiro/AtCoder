# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a = int(input())
    b = int(input())
    c = (a + b) % 12

    if c == 0:
        print(12)
    else:
        print(c)


if __name__ == "__main__":
    main()
