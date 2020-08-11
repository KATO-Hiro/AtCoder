# -*- coding: utf-8 -*-


def main():
    k, x = map(int, input().split())

    if 500 * k >= x:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
