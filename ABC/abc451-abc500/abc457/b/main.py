# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = []

    for _ in range(n):
        _, *ai = list(map(int, input().split()))
        a.append(ai)

    x, y = map(int, input().split())
    x -= 1
    y -= 1
    print(a[x][y])


if __name__ == "__main__":
    main()
