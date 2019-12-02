# -*- coding: utf-8 -*-


def main():
    x = int(input())

    if x < 100:
        print(0)
        exit()

    p, q = divmod(x, 100)

    if q <= p * 5:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    main()
