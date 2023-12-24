# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    b, g = map(int, input().split())

    if b > g:
        print("Bat")
    else:
        print("Glove")


if __name__ == "__main__":
    main()
