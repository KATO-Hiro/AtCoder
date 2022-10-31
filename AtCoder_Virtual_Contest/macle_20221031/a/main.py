# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x, a = map(int, input().split())

    if x < a:
        print(0)
    else:
        print(10)


if __name__ == "__main__":
    main()
