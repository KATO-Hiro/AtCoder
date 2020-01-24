# -*- coding: utf-8 -*-


def main():
    from itertools import product

    n = 10
    print(list(product(range(3), repeat=n)))


if __name__ == '__main__':
    main()
