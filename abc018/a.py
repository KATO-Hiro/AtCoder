# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


if __name__ == '__main__':
    points = [int(input()) for _ in range(3)]
    sorted_points = sorted(points)

    # See:
    # https://beta.atcoder.jp/contests/abc018/submissions/2274172
    for point in points:
        print(3 - sorted_points.index(point))
