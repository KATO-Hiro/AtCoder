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
    from itertools import accumulate

    input = sys.stdin.readline

    n, t = map(int, input().split())
    st = [tuple(map(int, input().split())) for _ in range(n)]
    u = []

    for si, ti in st:
        u.append(si)
        u.append(ti)

    compressed = compress_coordinate(u)
    imos = [0] * (2 * n + 10)

    for si, ti in st:
        start, end = compressed[si], compressed[ti]
        imos[start] += 1
        imos[end] -= 1

    imos = list(accumulate(imos))
    print(max(imos))


if __name__ == "__main__":
    main()
