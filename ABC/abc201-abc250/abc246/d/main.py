# -*- coding: utf-8 -*-


def f(a, b):
    return a ** 3 + a ** 2 * b + a * b ** 2 + b ** 3


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = float('inf')

    for a in range(10 ** 6 + 1):
        lower = -1
        upper = 10 ** 7

        while upper - lower > 1:
            mid = (lower + upper) // 2

            if f(a, mid) >= n:
                upper = mid
            else:
                lower = mid

        ans = min(ans, f(a, upper))

    print(ans)


if __name__ == "__main__":
    main()
