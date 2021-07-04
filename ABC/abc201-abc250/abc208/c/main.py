# -*- coding: utf-8 -*-


def compress_coordinate(elements: list) -> dict:
    ''' Means that reduce the numerical value while maintaining the magnitude
        relationship.
    Args:
        elements: list of integer numbers (greater than -1).
    Returns:
        A dictionary's items ((original number, compressed number) pairs).
    Landau notation: O(n log n)
    '''

    # See:
    # https://atcoder.jp/contests/abc036/submissions/5707999?lang=ja
    compressed_list = sorted(set(elements))
    return {element: index for index, element in enumerate(compressed_list)}


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    p, q = divmod(k, n)
    c = compress_coordinate(a)

    for ai in a:
        if c[ai] < q:
            print(p + 1)
        else:
            print(p)


if __name__ == "__main__":
    main()
