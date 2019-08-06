# -*- coding: utf-8 -*-


def main():
    n, a, b = map(int, input().split())

    if (b - a - 1) % 2 == 1:
        print('Alice')
    else:
        print('Borys')


if __name__ == '__main__':
    main()
