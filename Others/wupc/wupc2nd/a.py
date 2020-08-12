# -*- coding: utf-8 -*-


def main():
    n, m = map(int, input().split())
    total = 0

    for i in range(1, n + 1):
        total += i ** 2

    print(total % m)


if __name__ == '__main__':
    main()
