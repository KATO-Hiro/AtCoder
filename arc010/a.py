# -*- coding: utf-8 -*-


def main():
    n, m, a, b = map(int, input().split())
    c = [int(input()) for _ in range(m)]
    remain = n

    for day, ci in enumerate(c, 1):
        if remain <= a:
            remain += b

        remain -= ci

        if remain < 0:
            print(day)
            exit()

    print('complete')


if __name__ == '__main__':
    main()
