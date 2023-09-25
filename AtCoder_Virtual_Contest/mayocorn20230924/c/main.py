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

    n = len(s)
    t = run_length_encoding(list(s))

    counts = list()
    m = len(t)

    for j in range(m // 2):
        _, count1 = t[2 * j]
        _, count2 = t[2 * j + 1]

        count = count1 + count2

        if count % 2 == 0:
            counts.append((count // 2, count // 2))
        else:
            if count1 % 2 == 0:
                counts.append((count // 2, count // 2 + 1))
            else:
                counts.append((count // 2 + 1, count // 2))

    # print(t)
    # print(counts)
    ans = [0] * n
    id = 0

    for i in range(n - 1):
        if s[i] == "R" and s[i + 1] == "L":
            left_count, right_count = counts[id]
            ans[i] = left_count
            ans[i + 1] = right_count

            id += 1

    print(*ans)


if __name__ == "__main__":
    main()
