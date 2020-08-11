# -*- coding: utf-8 -*-


def main():
    a = sum(list(map(int, input().split())))
    b = sum(list(map(int, input().split())))
    print(max(a, b))


if __name__ == '__main__':
    main()
