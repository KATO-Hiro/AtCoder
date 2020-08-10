# -*- coding: utf-8 -*-


def main():
    from itertools import product

    n = int(input())

    # See:
    # https://docs.python.jp/3/library/itertools.html#itertools.product
    for j in sorted(list(product(['a', 'b', 'c'], repeat=n))):
        print(''.join(map(str, j)))


if __name__ == '__main__':
    main()
