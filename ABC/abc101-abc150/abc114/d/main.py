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
    ans = 0
    numbers = dict()

    for i in range(2, n + 1):
        r = run_prime_factorization(i)

        for key, value in r.items():
            if key not in numbers.keys():
                numbers[key] = value + 1
            else:
                numbers[key] += value

    count_75 = sum([1 for value in numbers.values() if value >= 75])
    count_25 = sum([1 for value in numbers.values() if value >= 25])
    count_15 = sum([1 for value in numbers.values() if value >= 15])
    count_5 = sum([1 for value in numbers.values() if value >= 5])
    count_3 = sum([1 for value in numbers.values() if value >= 3])

    # [75, ∞]が1つ以上
    ans += count_75

    # [25, ∞]が1つ以上, [3, 25)が1つ以上（[25, ∞]が1つのとき）
    count_3_24 = count_3 - count_25

    if count_25 > 0 and (count_25 - 1 + count_3_24) > 0:
        ans += count_25 * (count_25 - 1 + count_3_24)

    # [15, ∞]が1つ以上, [5, 15)が1つ以上（[15, ∞]が1つのとき）
    count_5_14 = count_5 - count_15

    if count_15 > 0 and (count_15 - 1 + count_5_14) > 0:
        ans += count_15 * (count_15 - 1 + count_5_14)

    # [5, ∞]が2つ以上, [3, 5)が1つ以上（[5, ∞]が2つのとき）
    count_3_4 = count_3 - count_5

    if count_5 > 1 and (count_5 - 2 + count_3_4) > 0:
        ans += (count_5 * (count_5 - 1) // 2) * (count_5 - 2 + count_3_4)

    print(ans)


if __name__ == "__main__":
    main()
