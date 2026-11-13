# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import pairwise

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * 3

    for ai, aj in pairwise(a):
        if aj > ai:
            ans[0] += 1
        elif aj < ai:
            ans[1] += 1
        else:
            ans[2] += 1

    print(*ans)


if __name__ == "__main__":
    main()
