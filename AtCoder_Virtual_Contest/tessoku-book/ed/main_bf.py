# -*- coding: utf-8 -*-


def digit_sum(n: int) -> int:
    summed = 0

    while n > 0:
        summed += n % 10
        n //= 10

    return summed


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = [i for i in range(1, n + 1)]

    for _ in range(k):
        b = [0] * n

        for i in range(n):
            b[i] = a[i] - digit_sum(a[i])

        a = b

    print(*a, sep="\n")


if __name__ == "__main__":
    main()
