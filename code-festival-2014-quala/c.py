# -*- coding: utf-8 -*-


def main():
    a, b = map(int, input().split())
    a -= 1
    print(b // 4 - b // 100 + b // 400 - (a // 4 - a // 100 + a // 400))


if __name__ == '__main__':
    main()
