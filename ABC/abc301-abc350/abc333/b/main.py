# -*- coding: utf-8 -*-


def f(first, second):
    # 各頂点に便宜的に整数を割り当てて、円周上の距離を求める
    dist = abs(get_offset(first) - get_offset(second))

    # 長い辺
    return dist == 2 or dist == 3


def get_offset(alphabet: str, base_alphabet: str = "A") -> int:
    """Get offset between the base_alphabet and alphabet.

    Args:
        alphabet: The alphabet to use.
        base_alphabet: The base alphabet to use.

    Returns:
        difference between the base_alphabet and alphabet.

    See:
    https://docs.python.org/3.11/library/functions.html?highlight=chr#ord
    """

    return ord(alphabet) - ord(base_alphabet)


def main():
    import sys

    input = sys.stdin.readline

    s1, s2 = list(input().rstrip())
    t1, t2 = list(input().rstrip())

    if f(s1, s2) == f(t1, t2):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
