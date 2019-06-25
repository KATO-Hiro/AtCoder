# -*- coding: utf-8 -*-


def main():
    a = int(input())
    b = int(input())
    e = int(input())
    g = a + b - e
    i = b + e - g
    f = a + g - e
    c = a + i - g
    d = b + c - g
    h = a + d - i

    print(a, b, c)
    print(d, e, f)
    print(g, h, i)


if __name__ == '__main__':
    main()
