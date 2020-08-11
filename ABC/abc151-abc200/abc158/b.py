# -*- coding: utf-8 -*-


def main():
    n, a, b = map(int, input().split())

    p, q = divmod(n, (a + b))

    print((p * a) + min(a, q))


if __name__ == '__main__':
    main()
