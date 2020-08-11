# -*- coding: utf-8 -*-


def main():
    a, b = map(int, input().split())

    if a == b:
        print(2 * a)
    else:
        print(2 * max(a, b) - 1)


if __name__ == '__main__':
    main()
