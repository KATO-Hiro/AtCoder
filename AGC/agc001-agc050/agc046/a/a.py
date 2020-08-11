# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    x = int(input())

    for i in range(1, 10 ** 6):
        if (i * x) % 360 == 0:
            print(i)
            exit()


if __name__ == '__main__':
    main()
