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

    s = list(input().rstrip())
    t = list(input().rstrip())

    rs = run_length_encoding(s)
    rt = run_length_encoding(t)

    if len(rs) != len(rt):
        print("No")
        exit()

    for (si, si_count), (ti, ti_count) in zip(rs, rt):
        if si != ti:
            print("No")
            exit()
        
        if si_count == 1 and ti_count >= 2:
            print("No")
            exit()

        if si_count > ti_count:
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()
