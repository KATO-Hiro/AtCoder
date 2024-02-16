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

    n, k = map(int, input().split())
    primes = run_prime_factorization(n)

    if sum(primes.values()) >= k:
        ans = list()

        for key, value in primes.items():
            for _ in range(value):
                ans.append(key)

        ans.sort()

        while len(ans) >= 2 and (len(ans) - 1) >= k:
            i = ans.pop()
            j = ans.pop()
            ans.append(i * j)

        print(*ans)
    else:
        print(-1)


if __name__ == "__main__":
    main()
