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
    results = run_length_encoding(list(s))
    m = len(results)
    ans = 0

    for i in range(m):
        if i + 2 >= m:
            break

        s1, count1 = results[i]
        s2, count2 = results[i + 1]
        s3, count3 = results[i + 2]

        if not (s1 == "J" and s2 == "O" and s3 == "I"):
            continue

        if (count1 >= count2) and (count3 >= count2):
            ans = max(ans, count2)

    print(ans)


if __name__ == "__main__":
    main()
