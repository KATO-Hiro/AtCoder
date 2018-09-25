# -*- coding: utf-8 -*-


def main():
    a = int(input())
    b = int(input())
    print(min(abs(a - b), 10 + b - a, 10 + a - b))


if __name__ == '__main__':
    main()
