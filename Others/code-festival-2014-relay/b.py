# -*- coding: utf-8 -*-


def main():
    a, s = map(int, input().split())

    if a >= s:
        print('Congratulations!')
    else:
        print('Enjoy another semester...')


if __name__ == '__main__':
    main()
