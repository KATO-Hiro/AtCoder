# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k, q = map(int, input().split())
    a = [0] * n

    for _ in range(q):
        xi, yi = map(int, input().split())
        xi -= 1

        a[xi] = yi
        b = sorted(a, reverse=True)
        print(sum(b[:k]))


if __name__ == "__main__":
    main()
