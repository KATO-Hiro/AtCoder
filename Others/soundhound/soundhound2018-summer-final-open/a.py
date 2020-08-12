# -*- coding: utf-8 -*-


def main():
    c, d = list(map(int, input().split()))
    n = 0
    count = 0

    while d > 140 * (2 ** n):
        count += max(0, min(d, 170 * (2 ** n)) - max(c, 140 * (2 ** n)))
        n += 1

    print(count)


if __name__ == '__main__':
    main()
