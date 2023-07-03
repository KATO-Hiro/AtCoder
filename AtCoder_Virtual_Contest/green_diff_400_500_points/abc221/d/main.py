# -*- coding: utf-8 -*-


def compress_coordinate(elements: list) -> dict:
    """Means that reduce the numerical value while maintaining the magnitude
        relationship.

    Args:
        elements: list of integer numbers (greater than -1).

    Returns:
        A dictionary's items ((original number, compressed number) pairs).

    Landau notation: O(n log n)
    """

    # See:
    # https://atcoder.jp/contests/abc036/submissions/5707999?lang=ja
    compressed_list = sorted(set(elements))
    return {element: index for index, element in enumerate(compressed_list)}


def main():
    import sys
    from collections import defaultdict
    from itertools import accumulate

    input = sys.stdin.readline

    n = int(input())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    c = list()

    for ai, bi in ab:
        c.append(ai)
        c.append(ai + bi)

    c1 = compress_coordinate(c)
    d = [0] * (len(c1) + 1)
    e = defaultdict(int)

    for ai, bi in ab:
        d[c1[ai]] += 1
        d[c1[ai + bi]] -= 1
        e[c1[ai]] = ai
        e[c1[ai + bi]] = ai + bi

    d = list(accumulate(d))
    count = defaultdict(int)

    for i, di in enumerate(d[:-1]):
        count[di] += e[i + 1] - e[i]

    ans = [0] * (n + 1)

    for i in range(1, n + 1):
        ans[i] = count[i]

    print(*ans[1:])


if __name__ == "__main__":
    main()
