# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    n = int(input())
    d = defaultdict(int)

    for _ in range(n):
        si = input().rstrip()

        if d[si] == 0:
            print(si)
        else:
            print(si + "(" + str(d[si]) + ")")

        d[si] += 1


if __name__ == "__main__":
    main()
