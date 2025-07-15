# -*- coding: utf-8 -*-


def convert_decimal_to_n_ary_number(n: int, m_ary_number: int = 2) -> str:
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

    for i in range(1, 10**6):
        si = str(i)

        # 偶数桁
        s = si + si[::-1]
        s2 = int(s)

        if s2 <= n:
            result = convert_decimal_to_n_ary_number(s2, a)

            if result == result[::-1]:
                ans += s2

        # 奇数桁
        # 中央の一つを削除
        t = si[:-1] + si[::-1]
        t2 = int(t)

        if t2 <= n:
            result = convert_decimal_to_n_ary_number(t2, a)

            if result == result[::-1]:
                ans += t2

    print(ans)


if __name__ == "__main__":
    main()
