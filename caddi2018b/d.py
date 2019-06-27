# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]

    for ai in a:
        if ai % 2 == 1:
            print('first')
            exit()

    print('second')


if __name__ == '__main__':
    main()
