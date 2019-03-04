# -*- coding: utf-8 -*-


def main():
    n, a, b = map(int, input().split())

    if a > b or (n == 1 and a != b):
        print(0)
    else:
        print(max(0, b - a) * (n - 1) + (a - b) + 1)


if __name__ == '__main__':
    main()
