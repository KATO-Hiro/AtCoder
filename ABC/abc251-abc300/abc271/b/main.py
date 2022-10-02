# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    l = [list(map(int, input().split())) for _ in range(n)]

    for i in range(q):
        si, ti = map(int, input().split())
        si -= 1

        print(l[si][ti])


if __name__ == "__main__":
    main()
