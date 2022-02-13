# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        ai, si = map(int, input().split())

        if (2 * ai <= si) and ((si - 2 * ai) & ai == 0):
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
