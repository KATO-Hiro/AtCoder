# -*- coding: utf-8 -*-


def main():
    from itertools import combinations
    import sys

    input = sys.stdin.readline

    n = int(input())
    d = list(map(int, input().split()))
    patterns = combinations(d, 2)
    ans = 0

    for p1, p2 in patterns:
        ans += p1 * p2

    print(ans)


if __name__ == "__main__":
    main()
