# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a = int(input())

    if 400 % a == 0:
        print(400 // a)
    else:
        print(-1)


if __name__ == "__main__":
    main()
