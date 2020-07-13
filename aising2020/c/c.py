# -*- coding: utf-8 -*-


def main():
    from math import sqrt
    import sys
    input = sys.stdin.readline

    # n = int(input())
    n = 10 ** 4
    m = int(sqrt(n))
    count = 0

    for i in range(1, n + 1):
        for x in range(1, m + 1):
            for y in range(m + 1, 0, -1):
                count += 1

    print(count)


if __name__ == '__main__':
    main()
