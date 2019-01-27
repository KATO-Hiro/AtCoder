# -*- coding: utf-8 -*-


def main():
    n, a, b = map(int, input().split())
    print(min(a, b), max(0, a + b - n))


if __name__ == '__main__':
    main()
