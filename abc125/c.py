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
    from fractions import gcd

    n = int(input())
    d = dict()
    a = list(map(int, input().split()))

    for ai in a:
        p = run_prime_factorization(ai)

        for key, pi in p.items():
            if key not in d.keys():
                d[key] = 1
            else:
                d[key] += 1

    ans = 1

    for key, val in sorted(d.items(), key=lambda x: x[1], reverse=True):
        if val == 3:
            ans *= key
        elif val == 2:
            ans *= key
            break

    for i in range(1, n):
        ans = max(ans, gcd(a[i - 1], a[i]))

    print(ans)


if __name__ == '__main__':
    main()
