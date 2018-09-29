# -*- coding: utf-8 -*-


def main():
    n = int(input())

    for i in range(100, 1000):
        if i % 111 == 0 and i >= n:
            print(i)
            exit()


if __name__ == '__main__':
    main()
