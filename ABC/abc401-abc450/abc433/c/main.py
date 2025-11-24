# -*- coding: utf-8 -*-


def run_length_encoding(iterable: list) -> list[list]:
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
    from itertools import pairwise

    input = sys.stdin.readline

    s = input().rstrip()
    results = run_length_encoding(list(s))
    ans = 0

    for first, second in pairwise(results):
        value1, count1 = first
        value2, count2 = second

        if int(value1) + 1 == int(value2):
            ans += min(count1, count2)

    print(ans)


if __name__ == "__main__":
    main()
