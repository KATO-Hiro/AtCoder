# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    for i in range(10 ** 5):
        if (i * (i + 1)) >= 2 * n:
            print(i)
            exit()


if __name__ == "__main__":
    main()
