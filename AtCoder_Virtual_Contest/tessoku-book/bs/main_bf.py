# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import permutations

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = float("inf")

    for ai in permutations(a):
        summed = 0

        for aij, bi in zip(ai, b):
            summed += aij * bi

        ans = min(ans, summed)

    print(ans)


if __name__ == "__main__":
    main()
