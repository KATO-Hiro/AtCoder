# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x = int(input())

    if x <= 10:
        print(10)
    elif x <= 15:
        print(15)
    else:
        print(17)


if __name__ == "__main__":
    main()
