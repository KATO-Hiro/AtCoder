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
    factorizations = dict()

    for i in range(2, n + 1):
        p = run_prime_factorization(i)

        for key, value in p.items():
            if key not in factorizations.keys():
                factorizations[key] = 1
            else:
                factorizations[key] += value

    for key in factorizations.keys():
        factorizations[key] += 1

    case1 = len([value for value in factorizations.values() if value >= 75])
    case2 = len([value for value in factorizations.values() if value >= 15])
    case3 = len([value for value in factorizations.values() if 5 <= value < 15])
    case4 = len([value for value in factorizations.values() if value >= 25])
    case5 = len([value for value in factorizations.values() if 3 <= value < 25])
    case6 = len([value for value in factorizations.values() if value >= 5])
    case7 = len([value for value in factorizations.values() if 3 <= value < 5])

    ans = 0
    ans += case1
    ans += max(0, case2 * (case2 - 1) // 2)
    ans += case2 * case3
    ans += max(0, case4 * (case4 - 1) // 2)
    ans += case4 * case5
    ans += max(0, case6 * (case6 - 1) * (case6 - 2) // 2)
    ans += max(0, case6 * (case6 - 1) // 2 * case7)
    print(ans)

    hoge = list()


if __name__ == '__main__':
    main()
