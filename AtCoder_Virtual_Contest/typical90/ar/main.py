# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    shift_count = 0

    for _ in range(q):
        ti, xi, yi = map(int, input().split())
        xi -= 1
        yi -= 1
        nxi = (xi - shift_count) % n
        nyi = (yi - shift_count) % n

        if ti == 1:
            a[nxi], a[nyi] = a[nyi], a[nxi]

        elif ti == 2:
            shift_count += 1
            shift_count %= n
        else:
            print(a[nxi])


if __name__ == "__main__":
    main()
