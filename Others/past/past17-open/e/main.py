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

    s = list(input().rstrip())

    results = run_length_encoding(s)
    ans = list()

    for result in results:
        ans.append(result[0])
        ans.append(str(result[1]))

    print(*ans)


if __name__ == "__main__":
    main()
