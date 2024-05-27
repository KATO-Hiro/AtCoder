# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import pairwise

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = a + b
    a = set(a)

    for ci, cj in pairwise(sorted(c)):
        if ci in a and cj in a:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
