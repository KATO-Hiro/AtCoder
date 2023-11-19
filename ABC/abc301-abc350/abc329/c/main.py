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
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    t = run_length_encoding(list(s))
    d = defaultdict(int)
    # print(t)

    for key, count in t:
        d[key] = max(d[key], count)

    ans = sum(d.values())
    print(ans)


if __name__ == "__main__":
    main()
