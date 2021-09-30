# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    k = int(input())
    a, b = input().split()
    a = list(reversed(a))
    b = list(reversed(b))

    x = 0
    y = 0

    for index, ai in enumerate(a):
        x += int(ai) * (k ** index)

    for index, ai in enumerate(b):
        y += int(ai) * (k ** index)

    print(x * y)


if __name__ == "__main__":
    main()
