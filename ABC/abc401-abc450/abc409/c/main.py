# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n, m = map(int, input().split())
    walls = [0] * (n + 1)

    for i in range(m):
        li, ri = map(int, input().split())
        li -= 1
        walls[li] += 1
        walls[ri] -= 1

    walls = list(accumulate(walls))
    print(min(walls[:n]))


if __name__ == "__main__":
    main()
