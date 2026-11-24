# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    c = Counter()

    for ai in a:
        for aij in ai:
            c[aij] += 1

    _, count = c.most_common()[0]
    print(n * m - count)


if __name__ == "__main__":
    main()
