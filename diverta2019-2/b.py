# -*- coding: utf-8 -*-


def main():
    n = int(input())
    xs = [0 for _ in range(n)]
    ys = [0 for _ in range(n)]
    d = dict()

    # KeyInsight (◯：気がつけた，△：解説を読んでなんとなく理解，×：理解できず):
    # ◯ 任意の二点について，ベクトルを計算
    # △ 同じベクトルの頻度を計算する
    # △ 頻度の最大値が減らせるコストの最大値
    # See:
    # https://www.youtube.com/watch?v=TbobvdA6AlE
    # https://atcoder.jp/contests/diverta2019-2/submissions/5920106
    for i in range(n):
        xi, yi = map(int, input().split())
        xs[i] = xi
        ys[i] = yi

    for j in range(n):
        for k in range(n):
            if j == k:
                continue

            c = xs[j] - xs[k], ys[j] - ys[k]

            if c in d:
                d[c] += 1
            else:
                d[c] = 1

    ans = n

    for di in d.values():
        ans = min(ans, n - di)

    print(ans)


if __name__ == '__main__':
    main()
