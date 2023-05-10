# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    sp = list()

    for i in range(n):
        si, pi = list(map(str, input().split()))
        sp.append((si, pi, i + 1))

    sp = sorted(sp, key=lambda x: (x[0], -int(x[1])))

    for _, _, id in sp:
        print(id)


if __name__ == "__main__":
    main()
