# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = [input().rstrip() for _ in range(n)]
    m = max([len(si) for si in s])

    for si in s:
        size = len(si)
        diff = (m - size) // 2
        print("." * diff + si + "." * diff)


if __name__ == "__main__":
    main()
