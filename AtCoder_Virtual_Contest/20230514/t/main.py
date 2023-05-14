# -*- coding: utf-8 -*-


# Define function shape.
def f(value, a, b):
    from math import sqrt

    return b * (value - 1) + a / sqrt(value)


def ternary_search():
    a, b = map(int, input().split())

    lower = 1  # TODO: Change lower value if necessary.
    upper = 10**18 + 1  # TODO: Change upper value if necessary.

    while lower + 2 < upper:
        left_center = (2 * lower + upper) // 3
        right_center = (lower + 2 * upper) // 3

        # >: min value, <: max value
        if f(left_center, a, b) > f(right_center, a, b):
            lower = left_center
        else:
            upper = right_center

    # Search for a range of integers if necessary.
    ans = float("inf")

    for i in range(max(1, int(lower - 5)), int(upper) + 5):
        ans = min(ans, f(i, a, b))

    print(ans)


def main():
    import sys

    input = sys.stdin.readline

    ternary_search()


if __name__ == "__main__":
    main()
