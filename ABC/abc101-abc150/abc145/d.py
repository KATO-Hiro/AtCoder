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
    large_x, large_y = map(int, input().split())
    x = -large_x + 2 * large_y
    y = 2 * large_x - large_y

    # ■ポイント1
    # 原点から(X, Y)に到達するには，
    # (i + 1, j + 2)をx回, (i + 2, j + 1)をy回操作する必要がある，と言い換える

    # 移動したマスの数と操作回数に関する連立方程式を立てる
    #  x + 2y = X
    # 2x +  y = Y
    # これを解くと，x = (-X + 2Y) / 3, y = (2X - y) / 3

    # 到達できないパターン：x, yが整数でないとき
    if x % 3 != 0 or y % 3 != 0:
        print(0)
        exit()

    # ■ポイント2
    # 組み合わせは，(x + y)回のうちx回もしくはy回を選ぶ方法と同じ
    xy = (x + y) // 3
    y = y // 3
    print(count_combination(xy, y))

    # 類題: ARC035B
    # https://atcoder.jp/contests/arc035/tasks/arc035_b


if __name__ == '__main__':
    main()
