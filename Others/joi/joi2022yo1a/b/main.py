# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x = int(input())
    y = int(input())
    z = int(input())

    if (x * 60 + y * 60) <= (z * 60 + 30):
        print(1) 
    else:
        print(0)


if __name__ == "__main__":
    main()
