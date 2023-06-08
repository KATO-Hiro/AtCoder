# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import product

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    mid = n // 2
    b, c = a[:mid], a[mid:]
    s = set()

    for pattern in product([0, 1], repeat=mid):
        summed = 0

        for pi, bi in zip(pattern, b):
            if pi == 1:
                summed += bi

        s.add(summed)

    for pattern in product([0, 1], repeat=n - mid):
        summed = 0

        for pi, bi in zip(pattern, c):
            if pi == 1:
                summed += bi

        if (k - summed) in s:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
