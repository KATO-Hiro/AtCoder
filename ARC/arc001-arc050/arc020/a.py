# -*- coding: utf-8 -*-


def main():
    a, b = map(int, input().split())

    if abs(a) < abs(b):
        print('Ant')
    elif abs(a) > abs(b):
        print('Bug')
    else:
        print('Draw')


if __name__ == '__main__':
    main()
