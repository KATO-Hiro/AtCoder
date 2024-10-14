# -*- coding: utf-8 -*-


# PyPy3でもTLE
def main():
    import sys
    from collections import defaultdict

    from atcoder.segtree import SegTree

    input = sys.stdin.readline

    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    inf = 10**18

    # (1st value, 1st count, 2nd value, 2nd count)
    def op(x, y):
        # value, countのペアに変換
        x_1st, x_2nd = (x[0], x[1]), (x[2], x[3])
        y_1st, y_2nd = (y[0], y[1]), (y[2], y[3])

        # 同じvalueのときは、countを合算
        value_count = defaultdict(int)

        for value, count in [x_1st, x_2nd, y_1st, y_2nd]:
            if value in value_count:
                value_count[value] += count
            else:
                value_count[value] = count

        # x, yにおける1st, 2ndのvalueとcountを取得
        value_count = sorted(value_count.items(), reverse=True)

        first_value, first_count = value_count[0]
        second_value, second_count = (
            value_count[1] if len(value_count) > 1 else (-inf, 0)
        )

        return first_value, first_count, second_value, second_count

    e = (-inf, 0, -inf + 1, 0)
    seg = SegTree(op, e, [(ai, 1, -inf, 0) for ai in a])

    for _ in range(q):
        qi, *args = map(int, input().split())

        if qi == 1:
            p, x = args
            p -= 1

            seg.set(p, (x, 1, -inf, 0))
        else:
            l, r = args
            l -= 1

            _, _, _, second_count = seg.prod(l, r)
            print(second_count)


if __name__ == "__main__":
    main()
