# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    m = list()

    for i in range(n):
        si, ti = input().rstrip().split()
        m.append((int(ti), si))

    sorted_m = sorted(m, reverse=True)
    print(sorted_m[1][1])


if __name__ == "__main__":
    main()
