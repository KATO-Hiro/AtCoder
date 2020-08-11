# -*- coding: utf-8 -*-


def main():
    a, b = map(int, input().split())
    print(max(a - 2 * b, 0))


if __name__ == '__main__':
    main()
