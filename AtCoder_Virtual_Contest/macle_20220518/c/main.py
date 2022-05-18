# -*- coding: utf-8 -*-


def nCr(n: int, r: int, mod=10 ** 9 + 7):
    result = 1

    for i in range(n, n - r, - 1):
        result *= i
        result %= mod
    
    for i in range(1, r + 1):
        result *= pow(i, mod - 2, mod)
        result %= mod
    
    return result


def main():
    import sys

    input = sys.stdin.readline

    n, a, b = map(int, input().split())
    mod = 10 ** 9 + 7
    # 全体 - 条件を満たさない場合を考える

    # ΣnCiの合計 = 2 ** n
    # 少なくとも1種類以上使用するので、 2 ** n - 1
    ans = pow(2, n, mod) - 1

    # nCa, nCbのa, bが小さいことを利用
    ans -= nCr(n, a, mod)
    ans -= nCr(n, b, mod)
    ans %= mod

    print(ans)


if __name__ == "__main__":
    main()
