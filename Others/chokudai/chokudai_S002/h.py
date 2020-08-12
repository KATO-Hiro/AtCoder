# -*- coding: utf-8 -*-


def main():
    n = int(input())

    for i in range(n):
        ai, bi = map(int, input().split())
        diff = abs(ai - bi)

        if diff == 0:
            print('-1')
        else:
            print(diff)


if __name__ == '__main__':
    main()
