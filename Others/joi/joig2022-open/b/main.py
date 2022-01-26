# -*- coding: utf-8 -*-


def main():
    from itertools import combinations
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = 0

    for x, y, z in combinations(a, 3):
        if x * y == z:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
