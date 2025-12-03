# -*- coding: utf-8 -*-


def calc_pascals_triangle(n_max, mod):
    """Calc binomial coefficients (nCk).

    Args:
        n_max: A max number (greater than or equal to 0).

    Returns:
        List of binomial coefficients.

    Examples:
        7C3: c[7][3]

    Landau notation: O(n_max ** 2).
    """

    assert n_max >= 0

    c = [[0 for _ in range(n_max + 1)] for _ in range(n_max + 1)]
    c[0][0] = 1

    for i in range(n_max):
        for j in range(i + 1):
            c[i + 1][j] += c[i][j] % mod
            c[i + 1][j + 1] += c[i][j] % mod

    return c


def solve(pascals_triangle, mod):
    n = int(input())
    c = list(map(int, input().split()))
    summed_c = 0
    ans = 1

    for ci in c:
        summed_c += ci
        ans *= pascals_triangle[summed_c][ci]
        ans %= mod

    print(ans)


def main():
    import sys

    input = sys.stdin.readline

    t, mod = map(int, input().split())
    c_max = 5000
    pascals_triangle = calc_pascals_triangle(c_max, mod)

    for _ in range(t):
        solve(pascals_triangle, mod)


if __name__ == "__main__":
    main()
