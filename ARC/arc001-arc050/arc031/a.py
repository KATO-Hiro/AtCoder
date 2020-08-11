# -*- coding: utf-8 -*-


def main():
    name = input()

    if name == name[::-1]:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
