# -*- coding: utf-8 -*-


def main():
    a, b, t = map(int, input().split())

    diff = b - a
    year = b

    while True:
        if year >= t:
            print(year)
            exit()

        year += diff


if __name__ == '__main__':
    main()
