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
    from itertools import pairwise

    input = sys.stdin.readline

    n = int(input())
    p = list(map(int, input().split()))
    q = list()

    for pi, pj in pairwise(p):
        if pi < pj:
            q.append("<")
        elif pi > pj:
            q.append(">")

    if len(set(q)) == 1:
        print(0)
        exit()

    rle = run_length_encoding(q)

    if q[0] == ">":
        rle = [("<", 0)] + rle
    if q[-1] == ">":
        rle = rle + [("<", 0)]

    m = len(rle)
    ans = 0

    for i in range(0, m, 2):
        if i + 2 >= m:
            break

        _, ci = rle[i]
        _, cj = rle[i + 2]

        ans += ci * cj

    print(ans)


if __name__ == "__main__":
    main()
