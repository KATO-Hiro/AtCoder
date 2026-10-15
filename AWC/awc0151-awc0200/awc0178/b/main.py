# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import pairwise

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = 0

    for ai, aj in pairwise(a):
        ans = max(ans, abs(ai - aj))

    print(ans)


if __name__ == "__main__":
    main()
