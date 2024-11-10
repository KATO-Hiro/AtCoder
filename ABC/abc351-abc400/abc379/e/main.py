# -*- coding: utf-8 -*-


from typing import List


def carry(n: int, digits: List[int]) -> List[int]:
    """Integer carry.

    Args:
        n     : Size of digits.
        digits: List of numbers. [0, digit, ..., digit]

    returns:
        List of numbers.

    Landau notation: O(n)
    """

    for pos in range(n - 1, 0, -1):
        p, q = divmod(digits[pos], 10)
        digits[pos] = q
        digits[pos - 1] += p

    if digits[0] == 0:
        digits = digits[1:]

    return digits


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    plus = [0]
    prev_plus = 0
    minus = [0]
    prev_minus = 0

    for i, si in enumerate(s):
        prev_plus += int(si)
        plus.append(prev_plus)

        prev_minus += int(si) * (n - i - 1)
        minus.append(prev_minus)

    for i, plus_i in enumerate(plus):
        plus[i] = plus_i * n

    ans = list()

    for pi, mi in zip(plus, minus):
        ans.append(pi - mi)

    ans = carry(n + 1, ans)
    print("".join(map(str, ans)))


if __name__ == "__main__":
    main()
