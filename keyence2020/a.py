# -*- coding: utf-8 -*-


def main():
    h = int(input())
    w = int(input())
    n = int(input())
    max_value = max(h, w)

    for i in range(10000 + 1):
        if max_value * i >= n:
            print(i)
            exit()


if __name__ == '__main__':
    main()
