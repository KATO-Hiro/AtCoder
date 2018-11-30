# -*- coding: utf-8 -*-


def main():
    from math import log10
    a = int(input())
    b = int(input())
    print(int((log10(a) + 1)) * int((log10(b) + 1)))


if __name__ == '__main__':
    main()
