# -*- coding: utf-8 -*-


def main():
    a, b, c = map(int, input().split())
    print(max(a * 10 + b + c, a + 10 * b + c, 10 * c + a + b))


if __name__ == '__main__':
    main()
