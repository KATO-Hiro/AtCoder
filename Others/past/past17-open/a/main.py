# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    w *= 100**2
    h2 = h**2

    if w < 20 * h2:
        print("A")
    elif 20 * h2 <= w < 25 * h2:
        print("B")
    else:
        print("C")


if __name__ == "__main__":
    main()
