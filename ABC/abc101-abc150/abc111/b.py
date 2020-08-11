# -*- coding: utf-8 -*-


def main():
    n = int(input())

    # See:
    # https://www.youtube.com/watch?v=fYS-rAUSD5o
    for i in range(111, 1000, 111):
        if i >= n:
            print(i)
            exit()


if __name__ == '__main__':
    main()
