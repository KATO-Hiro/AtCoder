# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = list()

    for i, ai in enumerate(a, 1):
        b.append((ai, i))

    b.sort(reverse=True)

    print(b[1][1])


if __name__ == "__main__":
    main()
