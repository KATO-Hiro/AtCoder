# -*- coding: utf-8 -*-


def main():
    from itertools import permutations

    n, m, l = map(int, input().split())
    p, q, r = map(int, input().split())

    ans = 0

    # KeyInsight
    # 90度回転する = p, q, rの並び順を全パターン試す
    # 各辺に入る箱の個数は、大きい箱の長さ / 小さい箱の長さを切り捨てたもの
    # See:
    # https://atcoder.jp/contests/arc013/submissions/74264
    for i, j, k in permutations((p, q, r), 3):
        ans = max(ans, (n // i) * (m // j) * (l // k))

    print(ans)


if __name__ == '__main__':
    main()
