# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    total = sum(a)

    for _ in range(q):
        xi, yi = map(int, input().split())
        xi -= 1

        diff = yi - a[xi]
        total += diff
        print(total)

        a[xi] = yi


if __name__ == "__main__":
    main()
