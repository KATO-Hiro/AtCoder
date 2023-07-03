# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = sorted(list(map(int, input().split())))
    n_max = a[-1]
    n_max_half = (n_max + 1) // 2
    diff = float("inf")
    r = -1

    for aj in a[:-1]:
        tmp = abs(aj - n_max_half)

        if tmp < diff:
            diff = tmp
            r = aj

    print(n_max, r)


if __name__ == "__main__":
    main()
