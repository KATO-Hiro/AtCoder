# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    d = int(input())
    x = int(input())
    a = [0, x] + [int(input()) for _ in range(d - 1)]
    b = list(accumulate(a))
    q = int(input())

    for _ in range(q):
        si, ti = map(int, input().split())

        if b[si] > b[ti]:
            print(si)
        elif b[si] < b[ti]:
            print(ti)
        else:
            print("Same")


if __name__ == "__main__":
    main()
