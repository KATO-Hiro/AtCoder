# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a = int(input())
    b = int(input())

    if (a + 7 * b) > 30:
        print(0)
    else:
        print(1)


if __name__ == "__main__":
    main()
