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


def ok(n, prime_factorization):
    for prime, prime_count in prime_factorization:
        m, count = n, 0

        while m > 0:
            count += m // prime
            m //= prime
        
        if count < prime_count:
            return False
    
    return True


def main():
    import sys

    input = sys.stdin.readline

    k = int(input())
    ps = run_prime_factorization(k).items()
    wa, ac = 1, k

    while ac - wa > 1:
        wj = (ac + wa) // 2

        if ok(wj, ps):
            ac = wj
        else:
            wa = wj

    print(ac)


if __name__ == "__main__":
    main()
