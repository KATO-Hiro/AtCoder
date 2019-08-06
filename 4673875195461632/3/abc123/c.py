# -*- coding: utf-8 -*-


def main():
    from math import ceil

    n = int(input())
    alpha = [int(input()) for _ in range(5)]
    print(max(0, ceil(n / min(alpha)) - 1) + 5)


if __name__ == '__main__':
    main()
