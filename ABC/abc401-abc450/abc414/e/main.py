# -*- coding: utf-8 -*-


def floor_decomposition(number):
    """
    count = floor(number / pos), left < pos <= right

    Returns a list of tuples (count, left, right) where:
        - count is the number of times the number can be divided by right
        - left is the next lower number that can be divided by count
        - right is the current divisor

    The process continues until right becomes zero.

    Landau's O(√n) algorithm is used to decompose the number.

    See:
    https://atcoder.jp/contests/abc414/submissions/67527693
    """

    results = []
    inf = 10**18
    right = inf

    while right:
        count = number // right
        left = number // (count + 1)

        results.append((count, left, right))
        right = left

    return results


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    mod = 998244353

    ans = n * (n + 1) // 2
    ans %= mod

    results = floor_decomposition(n)

    for count, left, right in results:
        ans -= count * (right - left)
        ans %= mod

    print(ans)


if __name__ == "__main__":
    main()
