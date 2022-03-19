# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    sp = list()

    for i in range(n):
        si, pi = input().rstrip().split()
        sp.append((si, int(pi), i + 1))
    
    sp = sorted(sp, key=lambda x: (x[0], -x[1]))

    for si, pi, i in sp:
        print(i)


if __name__ == "__main__":
    main()
