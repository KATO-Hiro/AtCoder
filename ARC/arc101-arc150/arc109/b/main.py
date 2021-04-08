# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    low = 1
    high = n + 1

    while (high - low) > 1:
        mid = (high + low) // 2

        if mid * (mid + 1) <= 2 * (n + 1):
            low = mid
        else:
            high = mid

    print(n - low + 1)


if __name__ == "__main__":
    main()
