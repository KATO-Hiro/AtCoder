# -*- coding: utf-8 -*-


def main():
    import sys
    from atcoder.segtree import SegTree

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    m = 2 * n + 2
    st = SegTree(max, 0, a[1::2])
    ans = 0

    for i in range(0, m, 2):
        value = st.prod(i // 2, n + 1)
        ans = max(ans, a[i] + value)

    print(ans)


if __name__ == "__main__":
    main()
