# -*- coding: utf-8 -*-


def main():
    a = int(input())

    for i in range(1, 100 + 1):
        if i ** 3 == a:
            print('YES')
            exit()

    print('NO')


if __name__ == '__main__':
    main()
