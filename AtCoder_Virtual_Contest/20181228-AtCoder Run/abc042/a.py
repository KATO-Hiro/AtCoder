# -*- coding: utf-8 -*-


def main():
    a = list(map(int, input().split()))

    if a.count(5) == 2 and a.count(7) == 1:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
