# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()

    if s.count("o") % 2 == 1:
        print("odd")
    else:
        print("even")


if __name__ == "__main__":
    main()
