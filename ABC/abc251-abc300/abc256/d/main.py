# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate
    import sys

    input = sys.stdin.readline

    n = int(input())
    size_max = 2 * 10 ** 5 + 100
    imos = [0] * (size_max)

    for i in range(n):
        li, ri = map(int, input().split())
        imos[li] += 1
        imos[ri] -= 1
    
    imos = list(accumulate(imos))
    start = False
    left = list()
    right = list()

    for i, value in enumerate(imos):
        if not start and value >= 1:
            start = True
            left.append(i)
        elif start and value == 0:
            start = False
            right.append(i)

    for li, ri in zip(left, right):
        print(li, ri)


if __name__ == "__main__":
    main()
