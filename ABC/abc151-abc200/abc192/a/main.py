# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x = int(input())

    print(100 - x % 100)


if __name__ == "__main__":
    main()
