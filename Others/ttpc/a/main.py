# -*- coding: utf-8 -*-


from typing import List


def generate_divisors(n: int) -> List[int]:
    '''
    Args:
        n: Int of number (greater than 0).
    Returns:
        List of divisors.
        (When n is less than or equal to 2 * 10 ** 5, the number of elements
         is at most 160.)
    Landau notation: O(√n)
    See:
    https://qiita.com/LorseKudos/items/9eb560494862c8b4eb56
    '''

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
    from math import gcd
    import sys

    input = sys.stdin.readline

    x, y = map(int, input().split())
    x -= 2015
    y -= 2015
    g = gcd(x, y)
    d = generate_divisors(g)
    print(*sorted(d), sep="\n")
    

if __name__ == "__main__":
    main()
