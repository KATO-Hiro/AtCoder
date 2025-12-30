# -*- coding: utf-8 -*-


def generate_divisors(n: int) -> list[int]:
    """
    Args:
        n: Int of number (greater than 0).

    Returns:
        List of divisors.
        (When n is less than or equal to 2 * 10 ** 5, the number of elements
         is at most 160.)

    Landau notation: O(√n)

    See:
    https://qiita.com/LorseKudos/items/9eb560494862c8b4eb56
    """

    lower_divisors, upper_divisors = [], []
    i = 1

    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)

            if i != n // i:
                upper_divisors.append(n // i)

        i += 1

    return lower_divisors + upper_divisors[::-1]


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    n, k = map(int, input().split())
    s = input().rstrip()
    periods = generate_divisors(n)
    ans = 10**18

    for period in periods:
        candidate = 0

        for i in range(period):
            j = i
            freq = Counter()

            while j < n:
                freq[s[j]] += 1
                j += period

            _, count = freq.most_common()[0]
            candidate += (n // period) - count

        if candidate > k:
            continue

        ans = min(ans, period)

    print(ans)


if __name__ == "__main__":
    main()
