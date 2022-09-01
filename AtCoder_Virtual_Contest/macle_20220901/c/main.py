# -*- coding: utf-8 -*-


def f(a, b_mid):
    summed = (a ** 3) + (a ** 2 * b_mid) + (a * b_mid ** 2) + (b_mid ** 3)

    return summed


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    value_max = 10 ** 6 + 1
    ans = float("inf")

    for a in range(value_max):
        b_min, b_max = -1, 10 ** 7

        while b_max - b_min > 1:
            b_mid = (b_min + b_max) // 2

            if f(a, b_mid) >= n:
                b_max = b_mid
            else:
                b_min = b_mid

        ans = min(ans, f(a, b_max))
    
    print(ans)


if __name__ == "__main__":
    main()
