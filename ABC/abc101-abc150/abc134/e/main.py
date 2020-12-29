# -*- coding: utf-8 -*-


def main():
    from collections import deque
    from bisect import bisect_left
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = [int(input()) for _ in range(n)]
    d = deque()

    for ai in a:
        index = bisect_left(d, ai)

        if index == 0:
            d.appendleft(ai)
        else:
            d[index - 1] = ai

    print(len(d))


if __name__ == "__main__":
    main()
