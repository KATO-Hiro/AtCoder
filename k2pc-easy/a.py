# -*- coding: utf-8 -*-


def main():
    a, b, c = map(int, input().split())
    n = int(input())
    print(max(n - a, 0), max(2 * n - b, 0), max(3 * n - c, 0))


if __name__ == '__main__':
    main()
