# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    n *= 1.08

    if int(n) > 206:
        print(":(")
    elif int(n) == 206:
        print("so-so")
    else:
        print("Yay!")


if __name__ == "__main__":
    main()
