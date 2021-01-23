# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    c = input()

    if c[0] == c[1] == c[2]:
        print("Won")
    else:
        print("Lost")


if __name__ == "__main__":
    main()
