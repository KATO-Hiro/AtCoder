# -*- coding: utf-8 -*-


def main():
    n = int(input())
    original = sorted('indeednow')

    for i in range(n):
        if sorted(input()) == original:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
