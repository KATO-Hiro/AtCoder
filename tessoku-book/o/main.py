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

    n = int(input())
    a = list(map(int, input().split()))
    c = compress_coordinate(a)
    b = list()

    for ai in a:
        b.append(c[ai] + 1)

    print(*b)


if __name__ == "__main__":
    main()
