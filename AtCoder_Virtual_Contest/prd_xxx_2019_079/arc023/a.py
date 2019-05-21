# -*- coding: utf-8 -*-


def count_days(y, m, d):
    return (365 * y + (y // 4) - (y // 100) + (y // 400) + ((306 * (m + 1)) // 10) + d - 429)


def main():
    y = int(input())
    m = int(input())
    d = int(input())

    if m == 1 or m == 2:
        m += 12
        y -= 1

    print(count_days(2014, 5, 17) - count_days(y, m, d))


if __name__ == '__main__':
    main()
