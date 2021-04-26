# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    if n < 2:
        print(0)
        exit()

    print(n - 2 + 1)


if __name__ == "__main__":
    main()
