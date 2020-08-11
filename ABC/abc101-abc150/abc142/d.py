# -*- coding: utf-8 -*-


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
    a, b = map(int, input().split())

    # KeyInsight:
    # x, yが互いに素であることと，x, yの最大公約数が1であることは同値
    # 素因数分解して，共通の素因数をすべて選ぶ
    count = 1
    result_a = run_prime_factorization(a)
    result_b = run_prime_factorization(b)
    count += len(result_a.keys() & result_b.keys())
    print(count)


if __name__ == '__main__':
    main()
