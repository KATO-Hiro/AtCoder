# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    n %= 4

    if n != 0:
        print("First")
    else:
        print("Second")


if __name__ == "__main__":
    main()
