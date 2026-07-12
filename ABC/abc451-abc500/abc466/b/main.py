# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    colors = [-1] * 101

    for _ in range(n):
        ci, si = map(int, input().split())
        colors[ci] = max(colors[ci], si)

    print(*colors[1 : m + 1])


if __name__ == "__main__":
    main()
