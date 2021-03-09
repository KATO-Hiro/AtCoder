# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = [int(input()) for _ in range(n)]
    s = sorted([si for si in s if si != 0], reverse=True)
    m = len(s)
    q = int(input())
    k = [int(input()) for _ in range(q)]

    for ki in k:
        if m <= ki:
            print(0)
        elif s[ki] == 0:
            print(0)
        else:
            print(s[ki] + 1)


if __name__ == "__main__":
    main()
