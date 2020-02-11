# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = len(set(a))

    if b == n:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
