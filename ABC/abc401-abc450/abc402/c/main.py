# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, m = map(int, input().split())
    remain = [0] * m
    d = defaultdict(list)

    for i in range(m):
        ki, *ai = map(int, input().split())
        remain[i] = ki

        for aij in ai:
            d[aij].append(i)

    b = list(map(int, input().split()))
    count = 0

    for bi in b:
        ai = d[bi]

        for aij in ai:
            remain[aij] -= 1

            if remain[aij] == 0:
                count += 1

        print(count)


if __name__ == "__main__":
    main()
