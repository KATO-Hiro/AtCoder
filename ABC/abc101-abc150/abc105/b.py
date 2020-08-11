# -*- coding: utf-8 -*-


def main():
    n = int(input())

    for i in range(0, 100 + 1):
        for j in range(0, 100 + 1):
            if (4 * i + 7 * j) == n:
                print('Yes')
                exit()

    print('No')


if __name__ == '__main__':
    main()
