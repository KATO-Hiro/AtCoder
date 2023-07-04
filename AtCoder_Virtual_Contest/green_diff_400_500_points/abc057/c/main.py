# -*- coding: utf-8 -*-


def count_digit(i):
    return len(list(str(i)))


def main():
    import sys
    from math import sqrt

    input = sys.stdin.readline

    n = int(input())
    values = set()

    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            values.add(n // i)
            values.add(i)

    ans = float("inf")

    for a in values:
        b = n // a
        ans = min(ans, max(count_digit(a), count_digit(b)))

    print(ans)


if __name__ == "__main__":
    main()
