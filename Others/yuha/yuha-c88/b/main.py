# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n = int(input())

    # See:
    # https://kmjp.hatenablog.jp/entry/2015/08/18/0900
    if n % 4 == 0:
        print('GO')
    else:
        print('SEN')


if __name__ == '__main__':
    main()
