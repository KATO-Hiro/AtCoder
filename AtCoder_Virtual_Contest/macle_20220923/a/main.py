# -*- coding: utf-8 -*-


def main():
    from math import floor   
    import sys

    input = sys.stdin.readline

    n = int(input())
    n *= 1.08
    n = floor(n)

    if n < 206:
        print("Yay!")
    elif n == 206:
        print("so-so")
    else:
        print(":(")


if __name__ == "__main__":
    main()
