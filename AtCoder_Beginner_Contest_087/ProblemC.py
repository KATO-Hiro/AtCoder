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

    # Init
    row_count = 2
    column_count = N

    candy_count = 0
    start_point_candy_count = route[0][0]
    end_point_candy_count = route[row_count - 1][column_count - 1]

    # Route choice.
    partly_candy_count = np.sum(route, axis=1)
    route1 = partly_candy_count[0] + end_point_candy_count
    route2 = partly_candy_count[1] + start_point_candy_count

    if route1 >= route2:
        candy_count = route1
    else:
        candy_count = route2

    # Output
    print(candy_count)
