# -*- coding: utf-8 -*-


def main():
    n = int(input())
    r_count = 0
    b_count = 0

    for i in range(n):
        si = input()
        r_count += si.count('R')
        b_count += si.count('B')

    if r_count > b_count:
        print('TAKAHASHI')
    elif r_count < b_count:
        print('AOKI')
    else:
        print('DRAW')


if __name__ == '__main__':
    main()
