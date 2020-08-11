# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    a, r, n = map(int, input().split())
    number = a

    if r == 1:
        print(a)
        exit()

    for i in range(1, n):
        number *= r

        if number > 10 ** 9:
            print('large')
            exit()

    print(number)


if __name__ == '__main__':
    main()
