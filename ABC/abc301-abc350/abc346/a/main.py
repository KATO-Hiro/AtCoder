# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import pairwise

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = list()

    for ai, aj in pairwise(a):
        ans.append(ai * aj)

    print(*ans)


if __name__ == "__main__":
    main()
