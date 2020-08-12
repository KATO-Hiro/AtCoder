# -*- coding: utf-8 -*-


def main():
    k = list(input())
    win_count = k.count('o')

    if (win_count + (15 - len(k))) >= 8:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
