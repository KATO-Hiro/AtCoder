# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b = input().rstrip().split()
    sum_a, sum_b = 0, 0

    for ai, bi in zip(list(a), list(b)):
        sum_a += int(ai)
        sum_b += int(bi)

    print(max(sum_a, sum_b))


if __name__ == "__main__":
    main()
