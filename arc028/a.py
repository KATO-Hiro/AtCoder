# -*- coding: utf-8 -*-


def main():
    n, a, b = map(int, input().split())
    count = 0

    while n > 0:
        if count % 2 == 0:
            n -= a
            if n <= 0:
                print('Ant')
                exit()
        else:
            n -= b
            if n <= 0:
                print('Bug')
                exit()

        count += 1


if __name__ == '__main__':
    main()
