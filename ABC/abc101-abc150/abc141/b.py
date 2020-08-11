# -*- coding: utf-8 -*-


def main():
    s = list(input())
    odd = s[::2]
    even = s[1::2]

    if 'L' not in odd and 'R' not in even:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
