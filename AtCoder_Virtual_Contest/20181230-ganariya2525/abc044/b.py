# -*- coding: utf-8 -*-


def main():
    from collections import Counter

    w = Counter(list(input()))

    for value in w.values():
        if value % 2 != 0:
            print('No')
            exit()

    print('Yes')


if __name__ == '__main__':
    main()
