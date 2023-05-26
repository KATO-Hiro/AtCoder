# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    rating = [0] * 9

    for ai in a:
        p, q = divmod(ai, 400)

        if p >= 8:
            rating[8] += 1
        else:
            rating[p] += 1

    summed = 0

    for i in range(8):
        if rating[i] > 0:
            summed += 1

    if summed > 0:
        print(summed, summed + rating[8])
    else:
        print(1, rating[8])


if __name__ == "__main__":
    main()
