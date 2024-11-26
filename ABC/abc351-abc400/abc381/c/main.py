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
    s = input().rstrip()
    results = run_length_encoding(list(s))
    m = len(results)
    ans = 1

    for i in range(1, m - 1):
        if results[i][0] != "/":
            continue

        if results[i - 1][0] == "1" and results[i][1] == 1 and results[i + 1][0] == "2":
            candidate = min(results[i - 1][1], results[i + 1][1]) * 2 + 1
            ans = max(ans, candidate)

    print(ans)


if __name__ == "__main__":
    main()
