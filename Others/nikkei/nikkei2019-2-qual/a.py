# -*- coding: utf-8 -*-


def main():
    from math import ceil

    n = int(input())
    count = 0

    for i in range(1, ceil(n / 2)):
        j = n - i

        if i != j:
            count += 1

    print(count)


if __name__ == '__main__':
    main()
