# -*- coding: utf-8 -*-


def main():
    h, w = list(map(int, input().split()))
    print(2 * h * w - (h + w))


if __name__ == '__main__':
    main()
