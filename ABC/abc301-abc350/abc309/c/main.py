# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n, k = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    s_ab = sorted(ab)
    b = list()

    for _, bi in s_ab:
        b.append(bi)

    b = [0] + list(accumulate(b))
    b_max = max(b)

    c = [b_max - bi for bi in b]
    prev = 0

    for (ai, _), ci in zip(s_ab, c):
        # print(ai, ci, ci <= k)
        if ci <= k:
            print(prev + 1)
            exit()

        prev = ai

    print(prev + 1)
    # print(s_ab)
    # print(b)
    # print(c)


if __name__ == "__main__":
    main()
