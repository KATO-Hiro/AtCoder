# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate
    import sys

    input = sys.stdin.readline

    n = int(input())
    first = [0 for _ in range(n)]
    second = [0 for _ in range(n)]

    for i in range(n):
        ci, pi = map(int, input().split())

        if ci == 1:
            first[i] = pi
        else:
            second[i] = pi
    
    first_acc = list(accumulate([0] + first))
    second_acc = list(accumulate([0] + second))

    q = int(input())

    for j in range(q):
        li, ri = map(int, input().split())

        ai = first_acc[ri] - first_acc[li - 1]
        bi = second_acc[ri] - second_acc[li - 1]

        print(ai, bi)


if __name__ == "__main__":
    main()
