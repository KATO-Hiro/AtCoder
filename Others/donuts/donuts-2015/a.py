# -*- coding: utf-8 -*-


def main():
    from math import pi

    r, d = map(int, input().split())
    print((r ** 2 * pi) * (2 * d * pi))


if __name__ == '__main__':
    main()
