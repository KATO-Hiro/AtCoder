# -*- coding: utf-8 -*-


def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if n < m:
        print('X')
    elif n > m:
        print('Y')
    else:
        for ai, bi in zip(a, b):
            if ai < bi:
                print('X')
                exit()
            elif ai > bi:
                print('Y')
                exit()

        print('Same')


if __name__ == '__main__':
    main()
