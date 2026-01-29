# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n, m = map(int, input().split())
    size = 3 * 10**5 + 100
    counts = [0] * size

    for _ in range(m):
        li, ri = map(int, input().split())

        if li > ri:
            li, ri = ri, li

        li -= 1

        counts[li] += 1
        counts[ri] -= 1

    acc = list(accumulate(counts))
    print(*acc[:n])


if __name__ == "__main__":
    main()
