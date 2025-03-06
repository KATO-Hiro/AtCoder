# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import pairwise

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))

    for ai, aj in pairwise(a):
        if ai >= aj:
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()
