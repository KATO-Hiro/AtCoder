# -*- coding: utf-8 -*-


def main():
    a, b = map(int, input().split())

    if b % a == 0:
        print(a + b)
    else:
        print(b - a)


if __name__ == '__main__':
    main()
