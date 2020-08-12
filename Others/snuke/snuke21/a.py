# -*- coding: utf-8 -*-


def main():
    from math import sqrt

    n = int(input())
    q = 1 + 8 * n

    if int(sqrt(q)) ** 2 == q:
        if (-1 + int(sqrt(q))) % 2 == 0:
            print((-1 + int(sqrt(q))) // 2)
        else:
            print(-1)
    else:
        print(-1)


if __name__ == '__main__':
    main()
