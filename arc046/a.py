# -*- coding: utf-8 -*-


def main():
    n = int(input())
    p, q = divmod(n, 9)

    if q == 0:
        result = [9] * p
    else:
        result = [q] * (p + 1)

    print(''.join(map(str, result)))


if __name__ == '__main__':
    main()
