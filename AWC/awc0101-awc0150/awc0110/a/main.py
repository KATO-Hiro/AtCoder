# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    s = list(map(int, input().split()))

    for _ in range(m):
        tj, vj = map(int, input().split())
        tj -= 1
        s[tj] = max(0, s[tj] + vj)

    print(*s)


if __name__ == "__main__":
    main()
