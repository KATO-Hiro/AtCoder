# -*- coding: utf-8 -*-


def main():
    s = input()
    f = int(s[:2])
    l = int(s[2:])

    if 1 <= f <= 12 and 1 <= l <= 12:
        print('AMBIGUOUS')
    elif 1 <= l <= 12:
        print('YYMM')
    elif 1 <= f <= 12:
        print('MMYY')
    else:
        print('NA')


if __name__ == '__main__':
    main()
