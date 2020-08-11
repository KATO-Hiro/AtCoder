# -*- coding: utf-8 -*-


def main():
    n = int(input())
    black_count = 0
    white_count = 0

    for i in range(n):
        si = input()

        if si == 'black':
            black_count += 1
        else:
            white_count += 1

    if black_count > white_count:
        print('black')
    else:
        print('white')


if __name__ == '__main__':
    main()
