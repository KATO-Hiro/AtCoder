# -*- coding: utf-8 -*-


def main():
    import sys
    from atcoder.lazysegtree import LazySegTree
    from operator import add

    input = sys.stdin.readline

    n = int(input())
    l = list(map(int, input().split()))
    orders = [0] * (n + 1)

    for i, li in enumerate(l, 1):
        orders[li] = i

    a = [i for i in range(n + 1)]
    inf = 10**18
    st = LazySegTree(min, inf, add, add, False, a)
    ans = []

    for order in orders:
        ans.append(st.get(order) + 1)

        st.apply(order, n + 1, -1)

    print(*ans[1:], sep="\n")


if __name__ == "__main__":
    main()
