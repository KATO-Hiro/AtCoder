# -*- coding: utf-8 -*-


def main():
    n, a, b = map(int, input().split())
    s = input()

    print(s[:a - 1] + s[a - 1:b][::-1] + s[b:])


if __name__ == '__main__':
    main()
