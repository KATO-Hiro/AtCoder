# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    r, x, y = map(int, input().split())
    count = 1

    if ((x ** 2) + (y ** 2)) < (r ** 2):
        print(2)
        exit()

    while ((r ** 2) * (count ** 2)) < ((x ** 2) + (y ** 2)):
        count += 1

    print(count)


if __name__ == "__main__":
    main()
