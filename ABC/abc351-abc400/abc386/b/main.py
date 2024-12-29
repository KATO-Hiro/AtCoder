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
    from math import ceil

    input = sys.stdin.readline

    s = input().rstrip()
    rle = run_length_encoding(list(s))
    ans = 0

    for key, count in rle:
        if key == "0":
            ans += ceil(count / 2)
        else:
            ans += count

    print(ans)


if __name__ == "__main__":
    main()
