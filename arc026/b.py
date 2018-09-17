# -*- coding: utf-8 -*-


def main():
    from math import sqrt

    n = int(input())
    numbers = set()

    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0 and i != n:
            numbers.add(i)

        p, q = divmod(n, i)

        if q == 0 and p != n:
            numbers.add(p)

    total = sum(numbers)

    if total == n:
        print('Perfect')
    elif total > n:
        print('Abundant')
    else:
        print('Deficient')


if __name__ == '__main__':
    main()
