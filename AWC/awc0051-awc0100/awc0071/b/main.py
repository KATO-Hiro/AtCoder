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
    rle = run_length_encoding(s)
    m = len(rle)
    ans = 0

    for i in range(m):
        if i + 2 >= m:
            break

        si, count1 = rle[i]
        sj, count2 = rle[i + 2]

        if si == sj:
            ans += count1 * count2

    print(ans)


if __name__ == "__main__":
    main()
