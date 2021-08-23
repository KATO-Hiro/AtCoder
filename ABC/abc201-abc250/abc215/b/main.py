# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    for k in range(100, -1, -1):
        if 2 ** k <= n:
            print(k)
            exit()


if __name__ == "__main__":
    main()
