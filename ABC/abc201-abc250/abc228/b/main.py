# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    taught = [False] * n

    while not taught[x - 1]:
        taught[x - 1] = True
        x = a[x - 1]

    print(sum(taught))


if __name__ == "__main__":
    main()
