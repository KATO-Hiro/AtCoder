# -*- coding: utf-8 -*-


def main():
    a, b = list(map(int, input().split()))

    if a * b > 0:
        print(b - a)
    else:
        print(b - a - 1)


if __name__ == '__main__':
    main()
