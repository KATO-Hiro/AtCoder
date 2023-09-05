# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x, y = input().rstrip().split(".")

    if int(y) >= 7:
        print(x + "+")
    elif int(y) >= 3:
        print(x)
    else:
        print(x + "-")


if __name__ == "__main__":
    main()
