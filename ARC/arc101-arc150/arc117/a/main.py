# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b = map(int, input().split())
    c = [i for i in range(1, a + 1)]
    d = [i for i in range(-1, -b - 1, -1)]
    diff = abs(a - b)

    if a > b:
        for j in range(diff):
            d[j % b] -= b + j + 1
    elif a < b:
        for j in range(diff):
            c[j % a] += a + j + 1

    print(*c, *d)


if __name__ == "__main__":
    main()
