# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a = int(input())
    b = int(input())
    c = int(input())

    summed = a + b + c

    if summed <= 21:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    main()
