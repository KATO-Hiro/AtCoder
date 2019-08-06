# -*- coding: utf-8 -*-
'''Snippets for factorization.
Available functions:
- run_prime_factorization: Run prime factorization.
'''


def run_prime_factorization(max_number: int) -> dict:
    '''Run prime factorization.
    Args:
        max_number: Int of number (greater than 1).
    Returns:
        A dictionary's items ((base, exponent) pairs).
    Landau notation: O(log n)
    '''

    from math import sqrt

    ans = dict()
    remain = max_number

    for base in range(2, int(sqrt(max_number)) + 1):
        if remain % base == 0:
            exponent_count = 0

            while remain % base == 0:
                exponent_count += 1
                remain //= base

            ans[base] = exponent_count

    if remain != 1:
        ans[remain] = 1

    return ans


def main():
    n = int(input())
    mod = 10 ** 9 + 7
    ans = 1
    d = dict()

    for i in range(2, n + 1):
        f = run_prime_factorization(i)

        for fi in f.keys():
            if fi not in d.keys():
                d[fi] = 1
            else:
                d[fi] += f[fi]

    for value in d.values():
        ans *= value + 1
        ans %= mod

    print(ans)


if __name__ == '__main__':
    main()
