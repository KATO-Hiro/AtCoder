# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    ans = float('inf')

    summed_a = sum(a)
    p, q = divmod(x, summed_a)
    candidate = p * n
    summed = 0

    for index, ai in enumerate(a, 1):
        summed += ai

        if summed > q:
            ans = min(ans, candidate + index)
            print(ans)
            exit()


if __name__ == "__main__":
    main()
