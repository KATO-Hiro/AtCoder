# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict
    from string import ascii_lowercase

    input = sys.stdin.readline

    x = input().rstrip()
    n = int(input())
    d = defaultdict(str)

    for xi, alpha in zip(x, ascii_lowercase):
        d[xi] = alpha

    names = list()

    for _ in range(n):
        si = input().rstrip()
        tmp = list()

        for sij in si:
            tmp.append(d[sij])

        names.append(("".join(tmp), si))

    for _, ans in sorted(names):
        print(ans)


if __name__ == "__main__":
    main()
