# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    pos = 0

    for _ in range(n):
        di, xi = input().rstrip().split()
        xi = int(xi)

        if di == "R":
            pos += xi
        else:
            pos -= xi

        print(pos)


if __name__ == "__main__":
    main()
