# -*- coding: utf-8 -*-


def main():
    k = int(input())
    s = input()
    n = len(s)

    if n > k:
        print(s[:k] + '...')
    else:
        print(s)


if __name__ == '__main__':
    main()
