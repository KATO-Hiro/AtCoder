# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n, m = map(int, input().split())
    size = 10**6 + 1
    counts = [0] * size

    for _ in range(m):
        li, ri = map(int, input().split())
        li -= 1
        counts[li] += 1
        counts[ri] -= 1

    acc = list(accumulate(counts))
    ans = 0

    for acc_i in acc[:-1]:
        if acc_i % 2 == 1:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
