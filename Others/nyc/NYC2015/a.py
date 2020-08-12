# -*- coding: utf-8 -*-


def main():
    n = bin(int(input()))[2:]

    if n == n[::-1]:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
