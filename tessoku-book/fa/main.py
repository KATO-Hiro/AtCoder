# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate
    import sys

    input = sys.stdin.readline

    d = int(input())
    a = [int(input()) for _ in range(d)]
    b = list(accumulate(a))
    q = int(input())

    for _ in range(q):
        si, ti = map(int, input().split())

        if b[si - 1] > b[ti - 1]:
            print(si)
        elif b[si - 1] < b[ti - 1]:
            print(ti)
        else:
            print("Same")


if __name__ == "__main__":
    main()
