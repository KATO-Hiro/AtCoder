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


def solve():
    from collections import Counter

    n = int(input())
    s = input().rstrip()

    rle = run_length_encoding(s)
    c = Counter(s)
    ans = 10**9

    for value, count in rle:
        now = (c[value] - count) * 2 + c[str(int(value) ^ 1)]
        ans = min(ans, now)

    print(ans)


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
