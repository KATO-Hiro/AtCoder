# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    print(max(0, n - 3))


if __name__ == "__main__":
    main()
