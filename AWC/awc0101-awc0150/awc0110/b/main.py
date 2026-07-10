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

    input = sys.stdin.readline

    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    results = run_length_encoding(s)
    ans = []

    for value, count in results:
        if count < k:
            continue

        ans += [value] * count

    print(*ans)


if __name__ == "__main__":
    main()
