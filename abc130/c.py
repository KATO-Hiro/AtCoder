# -*- coding: utf-8 -*-


def main():
    w, h, x, y = map(int, input().split())
    s = w * h / 2

    if h == 2 * y and w == 2 * x:
        print(s, 1)
    else:
        print(s, 0)


if __name__ == '__main__':
    main()
