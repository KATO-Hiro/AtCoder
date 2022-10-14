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
    import sys

    input = sys.stdin.readline

    n = int(input())
    p = run_prime_factorization(n)
    ans = 0

    for key, value in p.items():
        total = 0
        
        for i in range(1, 10):
            total += i

            if total == value:
                ans += i
                break
            elif total > value:
                ans += i - 1
                break

    print(ans)


if __name__ == "__main__":
    main()
