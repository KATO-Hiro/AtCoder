# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x = int(input())

    for i in range(1, 4):
        if i != x:
            print(i)
            exit()


if __name__ == "__main__":
    main()
