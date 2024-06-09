# -*- coding: utf-8 -*-

import numpy as np


def fractal(s, k, n):
    if k == n:
        return s
    else:
        s = np.tile(s, (1, 1))
        array1 = np.hstack((s, s, s))

        white = np.full((s.shape[0], s.shape[1]), ".")
        array2 = np.hstack((s, white, s))
        array = np.vstack((array1, array2, array1))

        return fractal(array, k + 1, n)


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = np.array([["#"]])
    result = fractal(s, 0, n)

    for res in result:
        print("".join(res))


if __name__ == "__main__":
    main()
