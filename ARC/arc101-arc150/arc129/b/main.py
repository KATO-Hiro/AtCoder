# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    left_max, right_min = 0, 10**18

    for _ in range(n):
        li, ri = map(int, input().split())

        left_max = max(left_max, li)
        right_min = min(right_min, ri)

        if left_max <= right_min:
            print(0)
        else:
            center = (left_max + right_min) // 2
            print(left_max - int(center))


if __name__ == "__main__":
    main()
