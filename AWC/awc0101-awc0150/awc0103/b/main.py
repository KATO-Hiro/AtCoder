# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    sum_a, sum_b = 0, 0

    for _ in range(n):
        ai, bi = map(int, input().split())
        sum_a += ai
        sum_b += bi

    print(min(sum_a, sum_b))


if __name__ == "__main__":
    main()
