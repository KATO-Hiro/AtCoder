# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, c = map(int, input().split())

    if c % 2 == 0:
        a = abs(a)
        b = abs(b)

    if a > b:
        print(">")
    elif a < b:
        print("<")
    else:
        print("=")


if __name__ == "__main__":
    main()
