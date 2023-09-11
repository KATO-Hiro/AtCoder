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

    s = input().rstrip()
    t = input().rstrip()
    n, m = len(s), len(t)

    if n > m:
        print("No")
        exit()
    elif n == m:
        if s == t:
            print("Yes")
            exit()
        else:
            print("No")
            exit()

    u = run_length_encoding(list(s))
    v = run_length_encoding(list(t))

    if len(u) != len(v):
        print("No")
        exit()

    for (ui, size_ui), (vi, size_vi) in zip(u, v):
        # print(ui, size_ui, vi, size_vi)

        if ui != vi:
            print("No")
            exit()
        elif size_ui > size_vi:
            print("No")
            exit()
        elif size_ui == 1 and size_vi >= 2:
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()
