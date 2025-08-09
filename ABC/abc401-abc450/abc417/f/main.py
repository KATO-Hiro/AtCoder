# -*- coding: utf-8 -*-


def main():
    import sys
    from atcoder.lazysegtree import LazySegTree

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    def op(a, b):
        return (a[0] + b[0], a[1] + b[1])

    e = (0, 0)

    def mapping(f, x):
        if f != ID:
            return (f * x[1], x[1])

        return x

    def composition(f, g):
        return g if f == ID else f

    ID = 8_000_000_000_000_000_000

    b = [(ai, 1) for ai in a]
    st = LazySegTree(op, e, mapping, composition, ID, b)
    mod = 998244353

    for _ in range(m):
        li, ri = map(int, input().split())
        li -= 1

        summed, count = st.prod(li, ri)
        inv = pow(ri - li, mod - 2, mod)  # 1 / p
        st.apply(li, ri, summed * inv % mod)

    ans = [0] * n

    for i in range(n):
        summed, _ = st.get(i)
        ans[i] = summed

    print(*ans)


if __name__ == "__main__":
    main()
