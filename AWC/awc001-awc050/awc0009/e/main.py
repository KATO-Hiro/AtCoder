# -*- coding: utf-8 -*-


def main():
    import sys
    from atcoder import segtree

    input = sys.stdin.readline

    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    inf = 10**18
    st_min = segtree.SegTree(min, inf, a)
    st_max = segtree.SegTree(max, -inf, a)

    for _ in range(q):
        li, ri = map(int, input().split())
        li -= 1

        value_min = st_min.prod(li, ri)
        value_max = st_max.prod(li, ri)
        ans = value_max - value_min
        print(ans)


if __name__ == "__main__":
    main()
