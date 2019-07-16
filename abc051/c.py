# -*- coding: utf-8 -*-


def main():
    sx, sy, tx, ty = map(int, input().split())
    first = list()
    second = list()

    for y in range(ty - sy):
        first.append('U')
        second.append('D')

    for x in range(tx - sx):
        first.append('R')
        second.append('L')

    third = ['L', 'U'] + first + ['R', 'D']
    fourth = ['R', 'D'] + second + ['L', 'U']

    print(''.join(map(str, first + second + third + fourth)))


if __name__ == '__main__':
    main()
