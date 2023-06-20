# -*- coding: utf-8 -*-


def convert_decimal_to_n_ary_number(n: int, m_ary_number: int = 2) -> int:
    """Represents conversion from decimal number to n-ary number.

    Args:
        n: Input number (greater than 1).
        m_ary_number: m-ary number (from 2 to 10).

    Returns:
        values of m-ary number.

    Landau notation: O(log n)
    """
    if n < m_ary_number:
        return n

    ans = ""

    while n >= m_ary_number:
        p, q = divmod(n, m_ary_number)
        n = p
        ans += str(q)

        if n < m_ary_number:
            ans += str(p)

    return int(ans[::-1])


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())

    for _ in range(k):
        n = convert_decimal_to_n_ary_number(int(str(n), 8), 9)
        n = int(str(n).replace("8", "5"))

    print(n)


if __name__ == "__main__":
    main()
