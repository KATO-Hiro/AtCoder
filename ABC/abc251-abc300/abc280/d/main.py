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


def f(n, p):
    if n == 0:
        return 0
    
    n //= p
    
    return n + f(n, p)


def main():
    import sys
    sys.setrecursionlimit(10 ** 7)

    input = sys.stdin.readline

    k = int(input())
    ps = run_prime_factorization(k).items()
    wa, ac = 1, k

    while ac - wa > 1:
        wj = (ac + wa) // 2
        ok = True

        for pi, count in ps:
            if f(wj, pi) < count:
                ok = False
                break

        if ok:
            ac = wj
        else:
            wa = wj

    print(ac)


if __name__ == "__main__":
    main()
