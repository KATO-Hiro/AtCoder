# -*- coding: utf-8 -*-


class Combination:
    """Count the total number of combinations.
    nCr % mod.
    nHr % mod = (n + r - 1)Cr % mod.

    Args:
        max_value: Max size of list. The default is 500,050
        mod      : Modulo. The default is 10 ** 9 + 7.

    Landau notation: O(n)

    See:
    http://drken1215.hatenablog.com/entry/2018/06/08/210000
    """

    def __init__(self, max_value=500050, mod=10**9 + 7):
        self.max_value = max_value
        self.mod = mod
        self.fac = [0 for _ in range(self.max_value)]
        self.finv = [0 for _ in range(self.max_value)]
        self.inv = [0 for _ in range(self.max_value)]

        self.fac[0] = 1
        self.fac[1] = 1
        self.finv[0] = 1
        self.finv[1] = 1
        self.inv[1] = 1

        for i in range(2, self.max_value):
            self.fac[i] = self.fac[i - 1] * i % self.mod
            self.inv[i] = self.mod - self.inv[self.mod % i] * (self.mod // i) % self.mod
            self.finv[i] = self.finv[i - 1] * self.inv[i] % self.mod

    def count_nCr(self, n, r):
        """Count the total number of combinations.
            nCr % mod.
            nHr % mod = (n + r - 1)Cr % mod.

        Args:
            n   : Elements. Int of number (greater than 1).
            r   : The number of r-th combinations. Int of number
                  (greater than 0).

        Returns:
            The total number of combinations.

        Landau notation: O(1)
        """

        if n < r:
            return 0
        if n < 0 or r < 0:
            return 0

        return self.fac[n] * (self.finv[r] * self.finv[n - r] % self.mod) % self.mod


def main():
    import sys

    input = sys.stdin.readline

    a, b, c, d = map(int, input().split())
    mod = 998244353
    comb = Combination(max_value=4 * 10**6 + 10, mod=mod)
    ans = 0

    # リンゴとオレンジを先に並べる
    # 最も右側のオレンジの右側にブドウを置く
    # 最も右側のリンゴの右側にバナナを置く

    # 最も右側のリンゴを境界として、左右に分ける
    # 左側: リンゴa個、オレンジb'個、右端をリンゴで固定
    # 右側: オレンジb - b'個、バナナc個、ブドウd個

    # b'を全探索
    for b1 in range(b + 1):
        count1 = comb.count_nCr(a + b1 - 1, b1)
        count2 = comb.count_nCr(b - b1 + c + d, c)
        ans += count1 * count2
        ans %= mod

    print(ans)


if __name__ == "__main__":
    main()
