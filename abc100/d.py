# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    xyz = [list(map(int, input().split())) for i in range(n)]
    candidates = [0 for _ in range(8)]
    signs = [[1, 1, 1], [1, 1, -1], [1, -1, 1], [-1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1], [-1, -1, -1]]

    for k in range(8):
        summed_xyz = [0 for _ in range(n)]
        i = 0

        for x, y, z in xyz:
            summed_xyz[i] = (x * signs[k][0]) + (y * signs[k][1]) + (z * signs[k][2])
            i += 1

        candidate = sorted(summed_xyz, reverse=True)
        candidates[k] = sum(candidate[:m])

    print(max(candidates))
