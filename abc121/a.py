# -*- coding: utf-8 -*-


def main():
    large_h, large_w = map(int, input().split())
    h, w = map(int, input().split())
    print((large_h - h) * (large_w - w))


if __name__ == '__main__':
    main()
