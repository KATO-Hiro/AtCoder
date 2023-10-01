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

    input = sys.stdin.readline

    n = int(input())
    results = run_prime_factorization(n)
    # print(results)
    ans = 0

    for value in results.values():
        for i in range(9, 0, -1):
            j = i * (i + 1) // 2

            if value >= j:
                # print(value, j)
                ans += i
                break

    print(ans)


if __name__ == "__main__":
    main()
