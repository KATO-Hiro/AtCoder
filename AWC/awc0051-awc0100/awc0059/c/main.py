# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    counts = [0] * (n + 1)

    for _ in range(m):
        lj, rj = map(int, input().split())
        lj -= 1
        counts[lj] += 1
        counts[rj] -= 1

    counts = list(accumulate(counts))
    p = []

    for ai, count in zip(a, counts):
        p.append(ai * count)

    print(*p)


if __name__ == "__main__":
    main()
