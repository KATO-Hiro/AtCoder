# -*- coding: utf-8 -*-


def main():
    n = int(input())
    k = int(input())

    if (k <= n) and ((n - k) % 2 == 0):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
