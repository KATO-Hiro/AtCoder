# -*- coding: utf-8 -*-


def nCr(n: int, r: int, mod=10 ** 9 + 7):
    '''Count the total number of combinations.
        nCr % mod.
        nHr % mod = (n + r - 1)Cr % mod.

    Args:
        n   : Elements. Int of number (greater than 1).
        r   : The number of r-th combinations. Int of number
                (greater than 0).

    Returns:
        The total number of combinations.

    Landau notation: O(n)
    '''    

    if n < r:
        return 0
    if n < 0 or r < 0:
        return 0

    result = 1

    for i in range(n, n - r, - 1):
        result *= i

    for i in range(1, r + 1):
        result //= i

    return result


def main():
    import sys

    input = sys.stdin.readline

    l = int(input())
    print(nCr(l - 1, 11, 2 ** 64))


if __name__ == "__main__":
    main()
