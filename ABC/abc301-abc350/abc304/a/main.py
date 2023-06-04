# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    sa = list()

    for i in range(n):
        si, ai = input().rstrip().split(" ")
        sa.append((int(ai), si, i))

    sb = sorted(sa, key=lambda x: x[0])

    i = sb[0][2]

    for j in range(i, i + n):
        print(sa[j % n][1])


if __name__ == "__main__":
    main()
