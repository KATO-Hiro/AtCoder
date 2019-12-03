# -*- coding: utf-8 -*-


def main():
    n = int(input())

    for x in range(1, 50000 + 1):
        if int(x * 1.08) == n:
            print(x)
            exit()

    print(':(')


if __name__ == '__main__':
    main()
