# -*- coding: utf-8 -*-


def main():
    n = int(input())

    p, q = divmod(n, 400)

    if q >= 1:
        p += 1

    print(p)


if __name__ == '__main__':
    main()
