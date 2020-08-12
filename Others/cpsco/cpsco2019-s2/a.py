# -*- coding: utf-8 -*-


def main():
    m, n = map(int, input().split())
    unit = m // n
    print(m - (unit * (n - 1)))


if __name__ == '__main__':
    main()
