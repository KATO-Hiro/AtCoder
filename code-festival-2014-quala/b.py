# -*- coding: utf-8 -*-


def main():
    a = input()
    b = int(input())
    print(a[b % len(a) - 1])


if __name__ == '__main__':
    main()
