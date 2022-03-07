# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, c, x = map(int, input().split())

    if x <= a:
        print(1)
    elif a + 1 <= x <= b:
        print(c / (b - a))
    else:
        print(0)


if __name__ == "__main__":
    main()
