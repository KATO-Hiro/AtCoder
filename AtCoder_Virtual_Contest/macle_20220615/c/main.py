# -*- coding: utf-8 -*-


from typing import List


def run_length_encoding(iterable: list) -> List[list]:
    '''
    Args:
        iterable: A list of numbers or strings.
    Returns:
        A list containing consecutive characters and their count.
    See:
    https://qiita.com/DaikiSuyama/items/07e237b7372e7c7b3432
    '''

    from itertools import groupby

    results = [[key, len(list(group))] for key, group in groupby(iterable)]

    return results


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    s = list(input().rstrip())

    results = run_length_encoding(s)
    groups = len(results)

    for i in range(k):
        if groups >= 3:
            groups -= 2
        elif groups == 2:
            groups = 1
    
    print(n - groups)


if __name__ == "__main__":
    main()
