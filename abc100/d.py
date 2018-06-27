# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


if __name__ == '__main__':
    from itertools import product
    from heapq import nlargest

    n, m = list(map(int, input().split()))
    xyz = [list(map(int, input().split())) for i in range(n)]
    ans = 0

    # See:
    # https://beta.atcoder.jp/contests/abc100/submissions/2691346
    for a, b, c in product((-1, 1), repeat=3):
        summed_xyz = [0 for _ in range(n)]
        i = 0

        for x, y, z in xyz:
            summed_xyz[i] = (x * a) + (y * b) + (z * c)
            i += 1

        ans = max(ans, sum(nlargest(m, summed_xyz)))

    print(ans)
