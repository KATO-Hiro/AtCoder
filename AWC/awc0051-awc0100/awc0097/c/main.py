# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import pairwise

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * n

    for i, (ai, aj) in enumerate(pairwise(a), 1):
        if ai > aj:
            ans[i] = i

    print(*ans)


if __name__ == "__main__":
    main()
