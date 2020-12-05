# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    left = 0
    right = 10 ** 9

    while (right - left) > 1:
        mid = (left + right) // 2

        k_count = 0

        for ai in a:
            k_count += (ai - 1) // mid

        result = k_count <= k

        if result:
            right = mid
        else:
            left = mid

    print(right)


if __name__ == "__main__":
    main()
