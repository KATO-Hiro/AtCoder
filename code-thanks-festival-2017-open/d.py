# -*- coding: utf-8 -*-


def main():
    n, m = map(int, input().split())

    if n < m:
        print(m - n)
    elif n % m == 0:
        print(0)
    else:
        print(m - 1)


if __name__ == '__main__':
    main()
