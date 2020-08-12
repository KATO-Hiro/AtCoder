# -*- coding: utf-8 -*-


def main():
    s = input()
    s = s.replace('hi', '')

    if len(s) == 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
