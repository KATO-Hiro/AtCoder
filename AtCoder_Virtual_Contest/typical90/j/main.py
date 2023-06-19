# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n = int(input())
    one, two = [0] * (n + 1), [0] * (n + 1)

    for i in range(1, n + 1):
        ci, pi = map(int, input().split())

        if ci == 1:
            one[i] = pi
        else:
            two[i] = pi

    one, two = list(accumulate(one)), list(accumulate(two))
    q = int(input())

    for _ in range(q):
        li, ri = map(int, input().split())
        li -= 1

        print(one[ri] - one[li], two[ri] - two[li])


if __name__ == "__main__":
    main()
