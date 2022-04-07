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

    h, w, n = map(int, input().split())
    ab = list()
    a = [0] * n
    b = [0] * n

    for i in range(n):
        ai, bi = map(int, input().split())
        a[i] = ai
        b[i] = bi

        ab.append((ai, bi))
    
    compressed_a = compress_coordinate(a)
    compressed_b = compress_coordinate(b)

    for ai, bi in ab:
        print(compressed_a[ai] + 1, compressed_b[bi] + 1)


if __name__ == "__main__":
    main()
