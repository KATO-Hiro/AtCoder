# -*- coding: utf-8 -*-


def run_length_encoding(iterable: list):
    '''
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

    # See:
    # https://blog.hamayanhamayan.com/entry/2019/09/11/203310_2
    results = run_length_encoding(s)
    group_count = len(results)

    for i in range(k):
        if group_count >= 3:
            group_count -= 2
        else:
            group_count = 1
    
    print(n - group_count)


if __name__ == "__main__":
    main()
