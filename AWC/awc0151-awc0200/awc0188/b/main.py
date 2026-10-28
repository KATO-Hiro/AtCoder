# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import pairwise

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = -1
    candidate = -1

    for i, (ai, aj) in enumerate(pairwise(a), 1):
        diff = aj - ai

        if diff <= candidate:
            continue

        candidate = diff
        ans = i

    print(ans)


if __name__ == "__main__":
    main()
