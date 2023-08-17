# -*- coding: utf-8 -*-


def lcm(a: int, b: int) -> int:
    """Compute least common multiple of a and b.

    Args:
        a: Int of number (greater than 0).
        b: Int of number (greater than 0).

    Returns:
        least common multiple.

    Landau notation: O(log n)

    See:
    https://gist.github.com/endolith/114336/eff2dc13535f139d0d6a2db68597fad2826b53c3
    https://docs.python.org/3/library/sys.html#sys.version_info
    """

    from math import gcd

    return a * b // gcd(a, b)


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    # n, m = 2, 20
    # a = [2, 4]

    # 整数として扱えるように、x = a[k] // 2 * (2 * p + 1)の形式に変形
    # 半公倍数に似ている公倍数の問題を考える
    # [1, m]の範囲にある公倍数lの個数countは、m // l

    # 2 * p + 1は必ず奇数となるため、以下の条件を追加で満たす必要がある
    # ・countには、b[k] * 偶数の場合も含まれているので除外
    # ・l // b[k]が偶数なら答えは0
    b = [ai // 2 for ai in a]
    lcm_all = 1

    for bk in b:
        lcm_all = lcm(lcm_all, bk)

    # print(lcm_all)

    count = m // lcm_all
    count = (count + 1) // 2

    for bk in b:
        if (lcm_all // bk) % 2 == 0:
            count = 0

    print(count)


if __name__ == "__main__":
    main()
