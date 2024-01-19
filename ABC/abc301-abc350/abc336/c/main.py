# -*- coding: utf-8 -*-


def convert_decimal_to_n_ary_number(n: int, m_ary_number: int = 2) -> str:
    """Represents conversion from decimal number to n-ary number.

    Args:
        n: Input number (greater than 1).
        m_ary_number: m-ary number (from 2 to 10).

    Returns:
        values of m-ary number.

    Landau notation: O(log n)
    """
    if n < m_ary_number:
        return str(n)

    ans = ""

    while n >= m_ary_number:
        p, q = divmod(n, m_ary_number)
        n = p
        ans += str(q)

        if n < m_ary_number:
            ans += str(p)

    return ans[::-1]


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    n -= 1
    results = convert_decimal_to_n_ary_number(n, 5)
    evens = [i for i in range(0, 10, 2)]
    # print(evens)
    # print(results)
    ans = list()

    for result in results:
        ans.append(evens[int(result)])

    print("".join(map(str, ans)))


if __name__ == "__main__":
    main()
