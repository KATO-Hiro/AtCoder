# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, c = map(int, input().split())

    if c % 2 == 0:
        if abs(a) > abs(b):
            print(">")
        elif abs(a) < abs(b):
            print("<")
        else:
            print("=")
    elif c % 2 == 1:
        if a > b:
            print(">")
        elif a < b:
            print("<")
        else:
            print("=")


if __name__ == "__main__":
    main()
