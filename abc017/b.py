# -*- coding: utf-8 -*-


def main():
    x = list(reversed(input()))
    i = 0

    while i < len(x):
        if x[i] in ['o', 'k', 'u']:
            i += 1
        elif x[i:i + 2] == ['h', 'c']:
            i += 2
        else:
            print('NO')
            exit()

    print('YES')


if __name__ == '__main__':
    main()
