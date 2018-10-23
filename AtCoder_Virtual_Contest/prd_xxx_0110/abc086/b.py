# -*- coding: utf-8 -*-


def main():
    from math import sqrt
    from math import ceil

    a, b = map(str, input().split())
    number = int(a + b)

    if ceil(sqrt(int(number))) ** 2 == int(number):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
