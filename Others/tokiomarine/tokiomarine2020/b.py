# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    a, v = map(int, input().split())
    b, w = map(int, input().split())
    t = int(input())

    if v == w:
        print('NO')
        exit()

    if a <= b:
        if 0 < ((b - a) / (v - w)) <= t:
            print('YES')
        else:
            print('NO')
    else:
        if 0 < ((b - a) / (w - v)) <= t:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
