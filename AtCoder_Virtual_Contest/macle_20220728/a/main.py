# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x, y, z = map(int, input().split())
    y /= x

    for i in range(10 ** 6, -1, -1):
        if y > (i / z):
            print(i)
            exit()


if __name__ == "__main__":
    main()
