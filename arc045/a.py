# -*- coding: utf-8 -*-


def main():
    s = input().split()
    result = list()

    for si in s:
        if si == 'Left':
            result.append('<')
        elif si == 'Right':
            result.append('>')
        else:
            result.append('A')

    print(' '.join(map(str, result)))


if __name__ == '__main__':
    main()
