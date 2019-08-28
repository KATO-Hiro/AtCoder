# -*- coding: utf-8 -*-


def main():
    n = int(input())
    vote_t, vote_a = 1, 1

    # See:
    # http://arc062.contest.atcoder.jp/data/arc/062/editorial.pdf
    # KeyInsight：各状態で，できるだけ得票数が少ないほうがよい
    # 高橋君にA票，青木君にB票あるとき，満たすべき比率がx：yだとすると，
    # A <= m * x ^ B <= m * yとなるような最小の自然数mを取ればよい
    for i in range(n):
        ti, ai = map(int, input().split())

        # 小数点の処理に注意
        m = max((vote_t - 1) // ti + 1, (vote_a - 1) // ai + 1)
        vote_t = ti * m
        vote_a = ai * m

    print(vote_t + vote_a)


if __name__ == '__main__':
    main()
