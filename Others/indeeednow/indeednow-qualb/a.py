# -*- coding: utf-8 -*-


def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    print(abs(x2 - x1) + abs(y2 - y1) + 1)


if __name__ == '__main__':
    main()
