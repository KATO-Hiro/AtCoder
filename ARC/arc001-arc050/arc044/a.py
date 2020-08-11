# -*- coding: utf-8 -*-


def main():
    n = int(input())

    # See:
    # https://www.slideshare.net/chokudai/arc044
    if n in [2, 3, 5]:
        print('Prime')
    elif (n == 1) or (n % 2 == 0) or (n % 3 == 0) or (n % 5 == 0):
        print('Not Prime')
    else:
        print('Prime')


if __name__ == '__main__':
    main()
