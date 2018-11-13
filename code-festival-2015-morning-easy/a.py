# -*- coding: utf-8 -*-


def main():
    from math import sqrt

    n = int(input())
    count = 0

    while True:
        if int(sqrt(n)) ** 2 == n:
            print(count)
            exit()

        n += 1
        count += 1


if __name__ == '__main__':
    main()
