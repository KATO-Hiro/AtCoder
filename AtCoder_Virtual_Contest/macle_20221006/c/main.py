# -*- coding: utf-8 -*-


def main():
    from math import ceil
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    a_max = max(a)
    b = [abs(ceil(a_max / 2) - ai) for ai in a]
    b_min = float("inf")
    candidate = float("inf")

    for ai, bi in zip(a, b):
        if ai == a_max:
            continue

        if bi < b_min:
            b_min = bi
            candidate = ai
    
    print(a_max, candidate)


if __name__ == "__main__":
    main()
