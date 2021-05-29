# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate

    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    summed_a = list(accumulate([0] + a))
    max_a = [0 for _ in range(n)]
    max_a[0] = a[0]

    for index, ai in enumerate(a[1:]):
        max_a[index + 1] = max(max_a[index], ai)

    delta = 0

    for index, ai in enumerate(a):
        delta += summed_a[index + 1]
        ans = delta + max_a[index] * (index + 1)
        print(ans)


if __name__ == "__main__":
    main()
