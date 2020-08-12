# -*- coding: utf-8 -*-


def main():
    n = int(input())
    n %= 40

    if 1 <= n <= 20:
        print(n)
    elif n == 0:
        print(1)
    else:
        print(41 - n)


if __name__ == '__main__':
    main()
