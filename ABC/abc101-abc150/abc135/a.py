# -*- coding: utf-8 -*-


def main():
    a, b = map(int, input().split())

    if ((a + b)) % 2 == 0:
        print((a + b) // 2)
    else:
        print('IMPOSSIBLE')


if __name__ == '__main__':
    main()
