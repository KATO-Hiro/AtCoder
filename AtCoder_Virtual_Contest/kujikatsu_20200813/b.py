# -*- coding: utf-8 -*-


def main():
    a, v = map(int, input().split())
    b, w = map(int, input().split())
    t = int(input())

    if v <= w:
        print('NO')
        exit()

    if a <= b:
        if 0 <= (b - a) <= t * (v - w):
            print('YES')
        else:
            print('NO')
    else:
        if 0 <= (a - b) <= t * (v - w):
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
