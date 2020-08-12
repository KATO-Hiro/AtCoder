# -*- coding: utf-8 -*-


def main():
    l, x, y, s, d = map(int, input().split())

    if s <= d:
        k = d - s
    else:
        k = d + l - s

    if y > x:
        print(min(k / (y + x), k / (y - x)))
    else:
        print(k / (y + x))


if __name__ == '__main__':
    main()
