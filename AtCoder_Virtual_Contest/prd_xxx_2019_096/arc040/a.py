# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = [list(input()) for _ in range(n)]
    red_count = 0
    blue_count = 0

    for i in range(n):
        for j in range(n):
            if s[i][j] == 'R':
                red_count += 1
            elif s[i][j] == 'B':
                blue_count += 1

    if red_count > blue_count:
        print('TAKAHASHI')
    elif red_count < blue_count:
        print('AOKI')
    else:
        print('DRAW')


if __name__ == '__main__':
    main()
