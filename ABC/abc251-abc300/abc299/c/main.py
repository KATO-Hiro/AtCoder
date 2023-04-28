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

    n = int(input())
    s = list(input().rstrip())
    t = run_length_encoding(s)

    if t[0][0] == "o":
        t = [['-', 0]] + t
        n += 1

    if t[-1][0] == "o":
        t = t + [['-', 0]]
        n += 1

    ans = -1

    for i, (si, count) in enumerate(t):
        if si == "o":
            if t[i - 1][1] >= 1 or t[i + 1][1] >= 1:
                ans = max(ans, count)

    print(ans)
    

if __name__ == "__main__":
    main()
