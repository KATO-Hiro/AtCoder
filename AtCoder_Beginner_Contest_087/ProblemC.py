# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

import numpy as np

if __name__ == '__main__':
    # Input
    N = int(input())
    route = np.zeros([2, N], dtype=int)

    # HACK: More smarter.
    for i in range(2):
        line = [int(i) for i in input().split(" ")]
        for j in range(N):
            route[i][j] = line[j]

    candy_count_max = 0

    # HACK: Not beautiful.
    # See: https://img.atcoder.jp/arc090/editorial.pdf
    # p.7
    for i in range(N):
        candy_count = 0

        for j in range(i + 1):
            candy_count += route[0][j]

        candy_count += route[1][i]

        for j in range(i + 1, N):
            candy_count += route[1][j]

        if candy_count > candy_count_max:
            candy_count_max = candy_count

    # Output
    print(candy_count_max)
