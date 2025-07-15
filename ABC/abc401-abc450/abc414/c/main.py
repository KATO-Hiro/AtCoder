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

    a = int(input())
    n = int(input())
    ans = 0

    # 偶数桁
    for i in range(1, 10**6):
        si = str(i)
        s = si + si[::-1]
        s2 = int(s)

        if s2 > n:
            break

        result = convert_decimal_to_n_ary_number(s2, a)

        if result == result[::-1]:
            ans += s2

    # 奇数桁
    for j in range(10**6):
        for center in range(10):
            tj = str(j)

            if j == 0:
                t = str(center)
            else:
                t = tj + str(center) + tj[::-1]

            t2 = int(t)

            if t2 > n:
                break

            result2 = convert_decimal_to_n_ary_number(t2, a)

            if result2 == result2[::-1]:
                ans += t2

    print(ans)


if __name__ == "__main__":
    main()
