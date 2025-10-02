# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(n)]

    for i, si in enumerate(s):
        for j, sij in enumerate(si):
            if sij == "#":
                continue

            print(i, j)


if __name__ == "__main__":
    main()
