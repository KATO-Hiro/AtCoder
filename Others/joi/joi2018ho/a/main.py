# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import pairwise

    input = sys.stdin.readline

    n, k = map(int, input().split())
    t = [int(input()) for _ in range(n)]
    diff = [second - (first + 1) for first, second in pairwise(t)]
    diff = sorted(diff, reverse=True)
    ans = max(t) + 1 - min(t) - sum(diff[: k - 1])
    print(ans)


if __name__ == "__main__":
    main()
