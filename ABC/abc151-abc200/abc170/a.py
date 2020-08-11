# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    x = list(map(int, input().split()))

    for index, xi in enumerate(x, 1):
        if xi == 0:
            print(index)
            exit()


if __name__ == '__main__':
    main()
