# -*- coding: utf-8 -*-


def main():
    n = int(input())

    if n == 1:
        print(1)
    else:
        print((n + (n * 6)) // 2)


if __name__ == '__main__':
    main()
