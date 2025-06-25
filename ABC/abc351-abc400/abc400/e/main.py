# -*- coding: utf-8 -*-

from math import sqrt


def solve(counts):
    ai = int(input())
    bi = int(sqrt(ai))

    while counts[bi] != 2:
        bi -= 1

    ans = bi**2
    print(ans)


def main():
    import sys

    input = sys.stdin.readline

    q = int(input())
    size_max = 10**6
    counts = [0] * (size_max + 1)

    for i in range(2, size_max + 1):
        if counts[i] >= 1:
            continue

        for j in range(i, size_max + 1, i):
            counts[j] += 1

    for _ in range(q):
        solve(counts)


if __name__ == "__main__":
    main()
