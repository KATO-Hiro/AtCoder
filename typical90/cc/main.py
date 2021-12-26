# -*- coding: utf-8 -*-


class TwoDimList:
    """
    See:
    https://atcoder.jp/contests/typical90/submissions/23891910
    """

    def __init__(self, h, w):
        self.h = h
        self.w = w
        self.arr = [0] * (h * w)

    def read(self, hi, wi):
        return self.arr[self.w * hi + wi]

    def insert(self, hi, wi, value):
        self.arr[hi * self.w + wi] = value

    def plus(self, hi, wi, value):
        self.arr[hi * self.w + wi] += value


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    size = 5001
    td = TwoDimList(size, size)

    for i in range(n):
        ai, bi = map(int, input().split())
        td.plus(ai, bi, 1)
    
    for j in range(size):
        for i in range(1, size):
            td.plus(j, i, td.read(j, i - 1))

    for i in range(size):
        for j in range(1, size):
            td.plus(j, i, td.read(j - 1, i))
    
    ans = 1

    for a in range(1, size):
        if a + k >= size:
            continue

        max_a = a + k

        for b in range(1, size):
            if b + k >= size:
                continue

            max_b = b + k
            candidate = td.read(max_a, max_b) - td.read(max_a, b - 1) - td.read(a - 1, max_b) + td.read(a - 1, b - 1)
            ans = max(ans, candidate)

    print(ans)
    

if __name__ == "__main__":
    main()
