# -*- coding: utf-8 -*-


def main():
    a, b = map(int, input().split())

    if (a * b) % 2 == 0:
        print('No')
    else:
        print('Yes')


if __name__ == '__main__':
    main()
