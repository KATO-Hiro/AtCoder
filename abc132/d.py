# -*- coding: utf-8 -*-


def count_combination(n: int, r: int, mod: int = 10 ** 9 + 7) -> int:
    '''Count the total number of combinations.
        nCr % mod.
        nHr % mod = (n + r - 1)Cr % mod.
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
        return count_combination(n, n - r, mod)

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


def main():
    n, k = map(int, input().split())
    mod = 10 ** 9 + 7

    # See:
    # http://drken1215.hatenablog.com/entry/2019/06/30/183400
    # https://atcoder.jp/contests/abc132/submissions/6205885
    for i in range(1, k + 1):
        blue_count = count_combination(k - 1, i - 1)

        if n - k + 1 >= i:
            red_count = count_combination(n - k + 1, i)
        else:
            red_count = 0

        ans = blue_count * red_count
        ans %= mod
        print(ans)


if __name__ == '__main__':
    main()
