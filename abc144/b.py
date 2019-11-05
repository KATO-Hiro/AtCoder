# -*- coding: utf-8 -*-


def main():
    n = int(input())

    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == n:
                print('Yes')
                exit()

    print('No')


if __name__ == '__main__':
    main()
