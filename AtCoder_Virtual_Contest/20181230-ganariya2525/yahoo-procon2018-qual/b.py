# -*- coding: utf-8 -*-


def main():
    x, k = map(int, input().split())
    x //= 10 ** k
    x += 1
    print(x * 10 ** k)


if __name__ == '__main__':
    main()
