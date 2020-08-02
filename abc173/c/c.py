# -*- coding: utf-8 -*-


def f(c, h_patterns, w_patterns, black_count):
    # マスを塗りつぶしたかどうか
    used = [[False for _ in range(len(w_patterns))]
            for _ in range(len(h_patterns))]

    for index, h_pattern in enumerate(h_patterns):
        if h_pattern != 1:
            continue

        for w_dash in range(len(w_patterns)):
            if not used[index][w_dash] and c[index][w_dash] == '#':
                used[index][w_dash] = True
                black_count -= 1

    for index, w_pattern in enumerate(w_patterns):
        if w_pattern != 1:
            continue

        for h_dash in range(len(h_patterns)):
            if not used[h_dash][index] and c[h_dash][index] == '#':
                used[h_dash][index] = True
                black_count -= 1

    return black_count


def main():
    from itertools import product

    h, w, k = map(int, input().split())
    c = [list(input()) for _ in range(h)]
    black_count = 0
    ans = 0

    # KeyInsight:
    # 制約からbit全探索をすると楽に実装できる
    # △: リストのコピーができていない=参照渡しの理解が不十分
    # △: 愚直に塗りつぶす行と列を決めて、その中に黒マスが含まれていたら減らす方針に
    for hi in range(h):
        for wi in range(w):
            if c[hi][wi] == '#':
                black_count += 1

    for h_patterns in product([1, 0], repeat=h):
        for w_patterns in product([1, 0], repeat=w):
            fi = f(c, h_patterns, w_patterns, black_count)

            if fi == k:
                ans += 1

    print(ans)


if __name__ == '__main__':
    main()
