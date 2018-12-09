# -*- coding: utf-8 -*-


def main():
    a, b, c = map(int, input().split())

    if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
        print(0)
    else:
        print(min(a * b, b * c, c * a))


if __name__ == '__main__':
    main()
