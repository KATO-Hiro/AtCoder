# -*- coding: utf-8 -*-


def main():
    a, b, k = map(int, input().split())

    if k - a < 0:
        print(a - k, b)
    else:
        if (k - a) - b < 0:
            print(0, b - (k - a))
        else:
            print(0, 0)


if __name__ == '__main__':
    main()
