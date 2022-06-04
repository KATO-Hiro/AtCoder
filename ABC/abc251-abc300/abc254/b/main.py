# -*- coding: utf-8 -*-


def calc_pascals_triangle(n_max):
    """Calc binomial coefficients (nCk).
    Args:
        n_max: A max number (greater than 0).
    Returns:
        List of binomial coefficients.
    Examples:
        7C3: c[7][3]
    Landau notation: O(n_max ** 2).
    """

    assert n_max > 0

    c = [[0 for _ in range(n_max + 1)] for _ in range(n_max + 1)]
    c[0][0] = 1

    for i in range(n_max):
        for j in range(i + 1):
            c[i + 1][j] += c[i][j]
            c[i + 1][j + 1] += c[i][j]

    return c


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    if n == 1:
        print(1)
        exit()

    c = calc_pascals_triangle(n - 1)

    for i, ci in enumerate(c):
        print(*c[i][:i + 1])


if __name__ == "__main__":
    main()
