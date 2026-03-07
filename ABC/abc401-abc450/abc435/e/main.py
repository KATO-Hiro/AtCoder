# -*- coding: utf-8 -*-

from bisect import bisect_left


def bisect_ge(sorted_array: list[int], value: int):
    """Find the smallest element >= x and its index, or None if it doesn't exist."""

    if sorted_array[-1] >= value:
        index: int = bisect_left(sorted_array, value)

        return index, sorted_array[index]

    return None, None


def main():
    import sys
    from itertools import pairwise
    from atcoder.lazysegtree import LazySegTree  # type: ignore

    input = sys.stdin.readline

    n, q = map(int, input().split())
    lr = [tuple(map(int, input().split())) for _ in range(q)]
    compressed = set([0, n])

    for li, ri in lr:
        compressed.add(li - 1)
        compressed.add(ri)

    compressed = sorted(compressed)
    # cell_count, node_count
    counts = [(second - first, 1) for first, second in pairwise(compressed)]

    def op(a, b):
        return (a[0] + b[0], a[1] + b[1])

    e = (0, 0)

    pending = -1

    def mapping(f, a):
        return a if f == pending else (f * a[1], a[1])

    def composition(f, g):
        return g if f == pending else f

    id = pending

    st = LazySegTree(op, e, mapping, composition, id, counts)

    for li, ri in lr:
        li -= 1

        left, _ = bisect_ge(compressed, li)
        right, _ = bisect_ge(compressed, ri)
        st.apply(left, right, 0)

        ans = st.all_prod()[0]
        print(ans)


if __name__ == "__main__":
    main()
