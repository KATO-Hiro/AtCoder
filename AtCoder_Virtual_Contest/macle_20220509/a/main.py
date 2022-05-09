# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    n = int(input())
    m = 10 ** 2
    d = defaultdict(int)

    for x in range(1, m + 1):
        for y in range(1, m + 1):
            for z in range(1, m + 1):
                result = x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x
                d[result] += 1

    for i in range(1, n + 1):
        print(d[i])


if __name__ == "__main__":
    main()
