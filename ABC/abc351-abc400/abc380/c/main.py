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

    n, k = map(int, input().split())
    s = input().rstrip()
    results = run_length_encoding(list(s))
    count = 0
    pos = -1

    for i, (key, _) in enumerate(results):
        if key == "1":
            count += 1

        if k == count:
            pos = i
            break

    # swap
    results[pos - 1], results[pos] = results[pos], results[pos - 1]
    ans = []

    for key, count in results:
        ans += [key] * count

    print("".join(ans))


if __name__ == "__main__":
    main()
