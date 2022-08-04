# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    n %= 500
    a = int(input())

    if n <= a:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
