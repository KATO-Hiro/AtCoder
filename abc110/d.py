# -*- coding: utf-8 -*-

mod = 10 ** 9 + 7


def mod_pow(a: int, p: int):
    '''a ** p % mod.'''

    if p == 0:
        return 1

    if p % 2 == 0:
        half_p = p // 2
        half = mod_pow(a, half_p)
        return (half ** 2) % mod
    else:
        return (a * mod_pow(a, p - 1)) % mod


def calc_combination(a: int, b: int):
    '''aCb % mod.'''

    if b > (a - b):
        return calc_combination(a, a - b)

    multiple = 1
    division = 1

    for i in range(b):
        multiple *= a - i
        division *= i + 1
        multiple %= mod
        division %= mod

    return multiple * mod_pow(division, mod - 2) % mod


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

            ans *= calc_combination(n + count - 1, n - 1)
            ans %= mod

    if remain != 1:
        ans *= calc_combination(n, 1)
        ans %= mod

    return ans


def main():
    n, m = map(int, input().split())

    # See:
    # https://www.youtube.com/watch?v=gdQxKESnXKs
    print(solve(n, m))


if __name__ == '__main__':
    main()
