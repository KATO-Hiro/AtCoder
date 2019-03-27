# -*- coding: utf-8 -*-


def main():
    s = input()
    t = ''

    for si in s[::-1]:
        if si == 'b':
            t += 'd'
        elif si == 'd':
            t += 'b'
        elif si == 'p':
            t += 'q'
        elif si == 'q':
            t += 'p'

    if s == t:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
