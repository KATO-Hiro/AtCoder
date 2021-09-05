# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    p = list(map(int, input().split()))
    q = [0] * n

    for index, pi in enumerate(p, 1):
        q[pi - 1] = index

    print(*q)


if __name__ == "__main__":
    main()
