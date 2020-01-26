# -*- coding: utf-8 -*-


def main():
    n = list(input())[::-1]
    even = sum(map(int, n[1::2]))
    odd = sum(map(int, n[::2]))
    print(even, odd)


if __name__ == '__main__':
    main()
