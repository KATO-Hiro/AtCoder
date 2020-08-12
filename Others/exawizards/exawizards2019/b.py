# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = input()

    red = s.count('R')
    blue = s.count('B')

    if red > blue:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
