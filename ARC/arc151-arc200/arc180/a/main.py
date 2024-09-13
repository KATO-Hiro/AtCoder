# -*- coding: utf-8 -*-

from typing import List


def run_length_encoding(iterable: list) -> List[list]:
    """
    Args:
        iterable: A list of numbers or strings.

    Returns:
        A list containing consecutive characters and their count.

    See:
    https://qiita.com/DaikiSuyama/items/07e237b7372e7c7b3432
    """

    from itertools import groupby

    results = [[key, len(list(group))] for key, group in groupby(iterable)]

    return results


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = list(input().rstrip())
    t = []

    # 偶数番目を反転させる
    for i, si in enumerate(s):
        if i % 2 == 1:
            if si == "A":
                t.append("B")
            else:
                t.append("A")
        else:
            t.append(si)

    result = run_length_encoding(t)
    ans = 1
    mod = 10**9 + 7

    for _, count in result:
        ans *= (count + 1) // 2
        ans %= mod

    print(ans)


if __name__ == "__main__":
    main()
