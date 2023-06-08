# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate, product

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    mid = n // 2
    b, c = a[:mid], set(list(accumulate((a[mid:]))))
    print(c)

    for pattern in product([0, 1], repeat=mid):
        summed = 0

        for pi, bi in zip(pattern, b):
            if pi == 1:
                summed += bi

        if (k - summed) in c:
            print("Yes")
            exit()
        print(pattern)
        print(summed)
    print(b, c)

    print("No")


if __name__ == "__main__":
    main()
