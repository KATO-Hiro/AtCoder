# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    y = int(input())

    for i in range(y, 3010):
        if i % 4 == 2:
            print(i)
            exit()


if __name__ == "__main__":
    main()
