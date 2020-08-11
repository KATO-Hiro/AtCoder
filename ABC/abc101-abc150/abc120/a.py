# -*- coding: utf-8 -*-


def main():
    a, b, c = map(int, input().split())
    print(min(b // a, c))


if __name__ == '__main__':
    main()
