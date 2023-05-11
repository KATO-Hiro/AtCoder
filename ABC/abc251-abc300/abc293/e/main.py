# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, x, m = map(int, input().split())

    # ⚪︎: 等比数列の和
    if a == 1:
        # △: 与えられた式を愚直に計算すると、分子は1ではなくx
        print(x % m)
    else:
        # △: mが素数でない場合への対処方法
        # mod m * (a - 1)を取る
        # See:
        # https://atcoder.jp/contests/abc293/editorial/5966
        # https://www.youtube.com/watch?v=O_ga06kO84Y

        # b = a ** n、k = a - 1とおく
        # 等比数列の和の式 % mは、(b / k) % m = rと言い換えられる
        # q, r = divmod(b / k, m)であることを利用すると、b / k = m * q + r
        # 両辺をk倍すると、b = (m * k) * q + r * k
        # 両辺に対して、mod mkをとると、b % mk = r * k
        # 両辺に対してkで割る
        k = a - 1
        ans = (pow(a, x, m * k) - 1) // k % m
        print(ans)


if __name__ == "__main__":
    main()
