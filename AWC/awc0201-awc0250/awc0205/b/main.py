# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import pairwise

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    ans = 0

    for si, sj in pairwise(s):
        if si != sj:
            continue

        ans += 1

    print(ans)


if __name__ == "__main__":
    main()
