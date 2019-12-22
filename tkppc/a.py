# -*- coding: utf-8 -*-


def main():
    n = int(input())

    for i in range(n):
        ai, bi = map(int, input().split())
        print(ai + bi)


if __name__ == '__main__':
    main()
