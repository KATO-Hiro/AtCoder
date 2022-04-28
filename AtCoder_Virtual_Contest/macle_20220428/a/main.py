# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b = map(int, input().split())

    if (a * b) % 2 == 0:
        print("Even")
    else:
        print("Odd")


if __name__ == "__main__":
    main()
