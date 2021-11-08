# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b  = map(int, input().split("."))

    if b >= 500:
        print(a + 1)
    else:
        print(a)


if __name__ == "__main__":
    main()
