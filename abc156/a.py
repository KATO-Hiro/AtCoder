# -*- coding: utf-8 -*-


def main():
    n, r = map(int, input().split())

    if n >= 10:
        print(r)
    else:
        print(100 * (10 - n) + r)


if __name__ == '__main__':
    main()
