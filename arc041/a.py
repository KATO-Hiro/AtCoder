# -*- coding: utf-8 -*-


def main():
    x, y = list(map(int, input().split()))
    k = int(input())

    if y >= k:
        print(x + k)
    else:
        print(x + 2 * y - k)


if __name__ == '__main__':
    main()
