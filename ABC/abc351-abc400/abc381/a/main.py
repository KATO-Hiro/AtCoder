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

    if "/" not in s:
        print("No")
        exit()

    results = run_length_encoding(list(s))
    m = len(results)

    if m == 1 and results[0][0] == "/":
        print("Yes")
    elif (
        m == 3
        and results[0][0] == "1"
        and results[1][0] == "/"
        and results[2][0] == "2"
        and results[1][1] == 1
        and results[0][1] == results[2][1]
    ):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
