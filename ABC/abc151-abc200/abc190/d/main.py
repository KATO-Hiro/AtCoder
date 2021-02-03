# -*- coding: utf-8 -*-


def main():
    from math import sqrt
    import sys

    input = sys.stdin.readline

    n = int(input())
    count = 0

    for digit in range(1, int(sqrt(2 * n)) + 1):
        a = (2 * n) - digit * (digit - 1)

        if a > 0 and a % (2 * digit) == 0:
            count += 1

    print(count * 2)


if __name__ == "__main__":
    main()
