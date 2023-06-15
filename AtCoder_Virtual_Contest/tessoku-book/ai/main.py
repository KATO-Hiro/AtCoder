# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))

    while n > 1:
        b = list()

        if n % 2 == 0:
            op = max
        else:
            op = min

        for ai, aj in zip(a, a[1:]):
            b.append(op(ai, aj))

        a = b
        n -= 1

    print(*a)


if __name__ == "__main__":
    main()
