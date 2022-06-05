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
        result %= mod

    for i in range(1, r + 1):
        result *= pow(i, mod - 2, mod)
        result %= mod

    return result


def main():
    import sys

    input = sys.stdin.readline

    x, y = map(int, input().split())
    mod = 10 ** 9 + 7

    # 操作1をa回、操作2をb回行うことで、(x, y)に到達できるかを判定
    a = - x + 2 * y
    b = 2 * x - y

    if a < 0 or b < 0 or a % 3 != 0 or b % 3 != 0:
        print(0)
        exit()
    
    a //= 3
    b //= 3

    # a + b C a
    ans = nCr(a +b, a)
    print(ans)


if __name__ == "__main__":
    main()
