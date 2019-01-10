# -*- coding: utf-8 -*-


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    p = int(input())

    print(min(a * p, b + max(0, (p - c)) * d))


if __name__ == '__main__':
    main()
