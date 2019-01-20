# -*- coding: utf-8 -*-

mod = 10 ** 9 + 7


'''Snippets for combination.

Available functions:
- count_combination: Count the total number of combinations.
'''


def count_combination(n: int, r: int, mod: int = 10 ** 9 + 7) -> int:
    '''Count the total number of combinations.
        nCr % mod.

    Args:
        n   : Elements. Int of number (greater than 1).
        r   : The number of r-th combinations. Int of number (greater than 0).
        mod : Modulo. The default is 10 ** 9 + 7.

    Returns:
        The total number of combinations.

    Landau notation: O(n)

    See:
    https://qiita.com/derodero24/items/91b6468e66923a87f39f
    '''

    if r > (n - r):
        return count_combination(n, n - r)

    if r == 0 or r == n:
        return 1

    if r == 1:
        return n

    multiple = 1
    division = 1

    for i in range(r):
        multiple *= n - i
        division *= i + 1
        multiple %= mod
        division %= mod

    return multiple * pow(division, mod - 2, mod) % mod


def solve(n: int, m: int):
    from math import sqrt

    ans = 1
    remain = m

    for j in range(2, int(sqrt(m)) + 1):
        if remain % j == 0:
            count = 0

            while remain % j == 0:
                count += 1
                remain //= j

            ans *= count_combination(n + count - 1, n - 1)
            ans %= mod

    if remain != 1:
        ans *= count_combination(n, 1)
        ans %= mod

    return ans


def main():
    n, m = map(int, input().split())

    # See:
    # https://www.youtube.com/watch?v=gdQxKESnXKs
    print(solve(n, m))


if __name__ == '__main__':
    main()
