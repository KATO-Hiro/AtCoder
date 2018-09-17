# -*- coding: utf-8 -*-


def main():
    from math import sqrt

    n = int(input())
    numbers = set()
    div_numbers = set()

    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0 and i != n:
            numbers.add(i)

    for number in numbers:
        p, q = divmod(n, number)

        if q == 0 and p != n:
            div_numbers.add(p)

    matched_numbers = numbers | div_numbers
    total = sum(matched_numbers)

    if total == n:
        print('Perfect')
    elif total > n:
        print('Abundant')
    else:
        print('Deficient')


if __name__ == '__main__':
    main()
