# -*- coding: utf-8 -*-


def main():
    from collections import Counter

    n = int(input())
    a = Counter([int(input()) for _ in range(n)])
    count = 0

    for value in a.values():
        count += value - 1

    print(count)


if __name__ == '__main__':
    main()
