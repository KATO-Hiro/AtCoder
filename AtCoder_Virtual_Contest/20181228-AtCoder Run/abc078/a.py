# -*- coding: utf-8 -*-


def main():
    x, y = input().split()

    if x > y:
        print('>')
    elif x < y:
        print('<')
    else:
        print('=')


if __name__ == '__main__':
    main()
