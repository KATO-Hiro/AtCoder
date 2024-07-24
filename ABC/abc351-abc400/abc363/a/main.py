# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    r = int(input())
    print(100 - r % 100)


if __name__ == "__main__":
    main()
