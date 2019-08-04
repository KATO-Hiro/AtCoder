# -*- coding: utf-8 -*-


def main():
    a, b, c = map(int, input().split())
    print(max(0, c - (a - b)))


if __name__ == '__main__':
    main()
