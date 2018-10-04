# -*- coding: utf-8 -*-


def main():
    n = int(input())

    if n <= 6:
        print(n * 15)
    elif (n >= 10) and (1 <= n % 10 <= 6):
        print(n // 10 * 100 + (n % 10) * 15)
    elif n % 10 == 0:
        print((n // 10) * 100)
    else:
        print((n // 10 + 1) * 100)


if __name__ == '__main__':
    main()
