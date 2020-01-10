# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]

    for b, c in zip(a, a[1:]):
        if c == b:
            print('stay')
        elif c > b:
            print('up', c - b)
        else:
            print('down', b - c)


if __name__ == '__main__':
    main()
