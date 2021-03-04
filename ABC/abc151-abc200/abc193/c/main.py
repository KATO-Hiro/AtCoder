# -*- coding: utf-8 -*-


def main():
    from math import sqrt
    import sys

    input = sys.stdin.readline

    n = int(input())
    m = set()

    for i in range(2, int(sqrt(n)) + 1):
        j = i
        j **= 2

        while j <= n:
            m.add(j)
            j *= i

    print(n - len(m))


if __name__ == "__main__":
    main()
