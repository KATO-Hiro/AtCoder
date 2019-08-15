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

    if (r > n) or (n < 0) or (r < 0):
        return 0

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
    p, q = divmod(k, n)

    if k >= n:
        # 可能な限り均等に分けると幸福度が最大となる
        # k % n個を配る組み合わせの問題に
        print(count_combination(n, q))
    else:
        # 全体の幸福度は必ず0になる
        # 均等に配る必要はなく，どんな配り方をしてもよい=重複を許した組み合わせ
        print(count_combination(n + k - 1, k))


if __name__ == '__main__':
    main()
