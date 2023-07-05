# -*- coding: utf-8 -*-


def run_prime_factorization(max_number: int) -> dict:
    """Run prime factorization.

    Args:
        max_number: Int of number (greater than 1).

    Returns:
        A dictionary's items ((base, exponent) pairs).

    Landau notation: O(log n)
    """

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
    from collections import Counter

    input = sys.stdin.readline

    n = int(input())
    mod = 10**9 + 7
    c = Counter()

    for i in range(2, n + 1):
        results = run_prime_factorization(i)

        for key, value in results.items():
            if key not in c.keys():
                c[key] = value
            else:
                c[key] += value

    ans = 1

    for value in c.values():
        ans *= value + 1
        ans %= mod

    # print(c)
    print(ans)


if __name__ == "__main__":
    main()
